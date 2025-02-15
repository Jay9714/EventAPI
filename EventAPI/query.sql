4. SQL Query:
"""
Write a custom SQL query to fetch the total tickets sold for all events along with event details. 
The query should optimize for large datasets and return the top 3 events by tickets sold.
"""

QUERY:-

SELECT * 
FROM event_api_event eae 
ORDER BY tickets_sold DESC
LIMIT 3