# Contributing

Thank you for considering an improvement to this project.

## Local workflow

1. Create a branch from `main`.
2. Make a focused change and keep the site dependency-free unless a dependency is clearly justified.
3. Run the regression tests:

   ```bash
   make test
   ```

4. Preview the site locally and check both desktop and mobile widths:

   ```bash
   make serve
   ```

5. Open `http://localhost:8000` and verify navigation, contact links, images, focus states, and responsive layout.
6. Submit a pull request that explains what changed and how it was tested.

## Style guidelines

- Use semantic HTML before adding custom behavior.
- Follow the existing HTML and CSS conventions unless a change is discussed first.
- Keep visual changes focused and verify them at desktop and mobile widths.
- Optimize images before committing them and include meaningful alternative text.
- Do not commit credentials, local environment files, generated output, or editor settings.
