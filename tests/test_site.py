"""Non-invasive regression tests for the existing static website."""

from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = PROJECT_ROOT / "index.html"
CSS_PATH = PROJECT_ROOT / "assets" / "css" / "galaksi-global.css"


class SiteParser(HTMLParser):
    """Collect HTML structure without modifying the production source."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.references: list[tuple[str, str]] = []
        self.image_alts: list[str | None] = []
        self.html_language: str | None = None
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)

        if tag == "html":
            self.html_language = attributes.get("lang")
        if tag == "title":
            self.in_title = True
        if element_id := attributes.get("id"):
            self.ids.append(element_id)
        if tag == "img":
            self.image_alts.append(attributes.get("alt"))

        for attribute in ("href", "src"):
            if reference := attributes.get(attribute):
                self.references.append((attribute, reference))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


class StaticSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = INDEX_PATH.read_text(encoding="utf-8")
        cls.css = CSS_PATH.read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_document_basics_are_present(self) -> None:
        self.assertTrue(self.html.lstrip().lower().startswith("<!doctype html>"))
        self.assertEqual(self.parser.html_language, "tr")
        self.assertEqual(self.parser.title.strip(), "Galaksi Global")

    def test_required_page_sections_are_present(self) -> None:
        required_ids = {"anasayfa", "hakkimizda", "hizmetler", "neden-biz", "teklif", "iletisim"}
        self.assertTrue(required_ids.issubset(self.parser.ids))
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)), "HTML IDs must be unique")

    def test_images_have_alt_text(self) -> None:
        self.assertTrue(self.parser.image_alts)
        for alt_text in self.parser.image_alts:
            self.assertIsNotNone(alt_text)
            self.assertTrue(alt_text.strip())

    def test_internal_links_have_targets(self) -> None:
        page_ids = set(self.parser.ids)
        for attribute, reference in self.parser.references:
            if attribute == "href" and reference.startswith("#"):
                self.assertIn(reference[1:], page_ids, f"Missing target for {reference}")

    def test_local_resources_exist_and_stay_inside_repository(self) -> None:
        external_schemes = {"http", "https", "mailto", "tel"}
        for _, reference in self.parser.references:
            parsed = urlsplit(reference)
            if parsed.scheme in external_schemes or reference.startswith("#"):
                continue

            local_path = (PROJECT_ROOT / unquote(parsed.path)).resolve()
            self.assertTrue(local_path.is_relative_to(PROJECT_ROOT.resolve()))
            self.assertTrue(local_path.is_file(), f"Missing local resource: {reference}")

    def test_css_assets_exist(self) -> None:
        for raw_reference in re.findall(r"url\([\"']?([^\"')]+)", self.css):
            if raw_reference.startswith(("data:", "http://", "https://")):
                continue
            asset_path = (CSS_PATH.parent / raw_reference).resolve()
            self.assertTrue(asset_path.is_file(), f"Missing CSS asset: {raw_reference}")

    def test_contact_links_are_available(self) -> None:
        references = {reference for _, reference in self.parser.references}
        self.assertIn("tel:+905432107830", references)
        self.assertIn("mailto:kubra@galaksiglobal.com", references)
        self.assertIn("tel:+905432107930", references)
        self.assertIn("mailto:muhasebe@galaksiglobal.com", references)

    def test_css_blocks_are_balanced(self) -> None:
        without_comments = re.sub(r"/\*.*?\*/", "", self.css, flags=re.DOTALL)
        self.assertEqual(without_comments.count("{"), without_comments.count("}"))


if __name__ == "__main__":
    unittest.main()
