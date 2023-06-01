from  .models import db 

import time

def mytask():
    while True:
        docs = db(db.document.status=="uploaded").select()
        for doc in docs:        
            print(f"processing doc {doc.id}")
            doc.update_record(status="processing")
            print("doing some processing")
            try:
                time.sleep(5)
                doc.update_record(status="processed")
                db.commit()
                print("done!")
            except:
                db.rollback()
                doc.update_record(status="failed")
                db.commit()
                print("failed!")
        print('sleeping')            
        time.sleep(10)