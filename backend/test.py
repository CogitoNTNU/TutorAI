from flashcards.knowledge_base.db_interface import MongoDB

if __name__ == '__main__':
    db = MongoDB()
    result = db.get_page_range("book", 1, 5)
    print(result)
    print(len(result))
