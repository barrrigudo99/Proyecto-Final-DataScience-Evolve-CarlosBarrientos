/**
 * fotocasa_scraper.js
 * ===================
 * Alternativa en Node.js + Puppeteer para Fotocasa.es.
 * Se usa JS en lugar de Python porque Fotocasa implementa fingerprinting
 * avanzado que resulta más fácil evadir con un navegador real en Node.
 *
 * Flujo:
 *   1. Lanza Puppeteer con un perfil de usuario realista
 *   2. Itera sobre páginas de resultados de alquiler
 *   3. Extrae precio, metros, habitaciones, localización y URL
 *   4. Guarda en data/raw/fotocasa_raw.json
 *
 * Uso:
 *   node 00_scraping/fotocasa_scraper.js
 *   node 00_scraping/fotocasa_scraper.js --ciudad barcelona --paginas 3
 */

// TODO: const puppeteer = require('puppeteer-extra') con StealthPlugin
// TODO: función scrapeListado(ciudad, maxPaginas) → array de objetos
// TODO: exportar a JSON con fs.writeFileSync
