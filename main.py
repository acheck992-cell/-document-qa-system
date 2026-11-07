class DocumentQASystem:
    def __init__(self):
        # Sample knowledge base representing document content
        self.kb = {
            "python": "Python is a high-level programming language widely used in data science, artificial intelligence, and web development.",
            "internship": "An internship provides practical industry exposure and hands-on project experience for students and beginners.",
            "machine learning": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience."
        }

    def get_answer(self, question):
        question = question.lower()
        for keyword, details in self.kb.items():
            if keyword in question:
                return details
        return "Information regarding this query is currently not available in the document repository."

if __name__ == "__main__":
    qa = DocumentQASystem()
    print("--- Document Question-Answering System ---")
    
    sample_query = "Tell me about Python"
    print(f"Query: {sample_query}")
    print("Answer:", qa.get_answer(sample_query))
