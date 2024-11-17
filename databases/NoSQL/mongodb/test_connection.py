from pymongo import MongoClient

def test_connection():
        try:
                    # Connect to MongoDB
                            client = MongoClient('mongodb://localhost:27017/')
                                    
                                            # Check the server status
                                                    server_info = client.server_info()  # Will raise an exception if unable to connect
                                                            print("Connection to MongoDB successful!")
                                                                    print("Server Information:", server_info)

                                                                        except Exception as e:
                                                                                    print("Could not connect to MongoDB:", e)

                                                                                    if __name__ == "__main__":
                                                                                            test_connection()

