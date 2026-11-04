export default defineAppConfig({
  // Configure Content Wind here
  cover: '/logo.svg',
  // Home page hero photos (up to three), shown like prints on a table.
  // Put files in public/images/hero/ and list them here, e.g.
  // { src: '/images/hero/1985-block-party.jpg', alt: 'Neighbors at a 1985 block party', caption: 'Block party, 1985' }
  // While the list is empty, the hero shows the association badge.
  heroPhotos: [] as { src: string, alt: string, caption?: string }[],
  socials: {
    github: 'woodmont-civic/woodmont-civic.github.io',
    facebook: 'https://www.facebook.com/profile.php?id=100064680700200',
  },
  prose: {
    h1: {
      icon: 'akar-icons:air'
    }
  }
})
