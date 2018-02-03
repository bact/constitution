# constitution
Convert Thai constitution from PDF to plaintext and correct encoding glitches

- Use [Apache PDFBox](https://pdfbox.apache.org/) for PDF to HTML conversion
- Convert Thai characters that encoded as HTML entities to UTF-8
- Correct wrong order of Thai characters, like <tonemark><vowel> --> <vowel><tonemark>
- Basic reformatting

Ideally, there should be no need for a script like this. All laws should be available in search friendly and machine-readable format.
