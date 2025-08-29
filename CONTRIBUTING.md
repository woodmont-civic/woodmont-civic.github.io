# Contributing to Woodmont Civic Association Website

## Adding the Neighborhood Covenant PDF

The current `public/neighborhood-covenant.pdf` is a placeholder. To add the actual document:

1. **Replace the placeholder**: Delete the current `public/neighborhood-covenant.pdf` file
2. **Add the real PDF**: Copy your actual Neighborhood Covenant PDF to `public/neighborhood-covenant.pdf`
3. **Test locally**: Run `yarn dev` to ensure the PDF loads correctly
4. **Create a PR**: The preview will show your changes before merging

## Image Guidelines

- **Cover images**: Use SVG format for better quality and smaller file sizes
- **Photos**: Use JPG for photos, PNG for images requiring transparency
- **File sizes**: Keep images under 1MB for optimal loading
- **Dimensions**: Cover images should be 1200x800 pixels or similar aspect ratio

## Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test locally: `yarn dev`
5. Commit: `git commit -m "Description of changes"`
6. Push: `git push origin feature-name`
7. Create a Pull Request
8. Review the preview URL
9. Merge after approval

## File Structure

- `content/` - Markdown content files
- `public/` - Static assets (PDFs, images, etc.)
- `pages/` - Vue.js page components
- `.github/workflows/` - GitHub Actions for deployment
