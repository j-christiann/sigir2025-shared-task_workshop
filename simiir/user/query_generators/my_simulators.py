from .base import Base # Corrected import based on your directory structure

class SimpleUser(Base):
    """
    Simulator 1: Submits the initial query, then repeats it twice before stopping.
    """
    def generate_query(self, topic, serp, history):
        # 1. Start Session: Use the topic title as the first query
        if not history.query_count():
            # topic.get_title() is the Topic field from your input file
            return topic.get_title() 

        # 2. Limit Check: Stop after 3 queries total
        if history.query_count() >= 3:
            return None # None means the simulation session stops

        # 3. Repeat: Otherwise, repeat the last query submitted
        # history.get_last_query() returns the previous query string
        return history.get_last_query()

class KeywordReformulator(Base):
    """
    Simulator 2: Performs Query Expansion based on the last clicked document (You fill in the logic).
    """
    MAX_QUERIES = 7 

    def generate_query(self, topic, serp, history):
        # ... Implementation of your complex query expansion logic goes here ...
        
        # NOTE: You may also need to import code from 'additional_terms.py' 
        # or 'bi_term.py' to help with keyword extraction if those contain utility functions.
        
        return "your new, reformulated query string"
