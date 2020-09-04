# scrape_local
Search for local businesses that might want web/IT/marketing services

- Use API and web scraping to download news items (News API, local newspapers, community boards)
    - REMOVED: replacing with postgresql queries of business info from Philly Open Data
- Text processing to determine news items meet criteria
    - REMOVED: searching based on industry with above process does not require text processing
- Store info in local DB
    - Info stored on MongoDB
- API/web scraping for contact info
- Send out alerts based on business type - prefabricated pitch to meet their needs