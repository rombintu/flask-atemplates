from model import Templates
from main import UPLOAD_FOLDER

import os 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


files=[]
files = [f for f in sorted(os.listdir(UPLOAD_FOLDER))]
for i, file in enumerate(files):
    print(f"[{i}]: {file}")

user_input = int(input('DELETE [N]: '))

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
temp = session.query(Templates).filter(Templates.path==files[user_input]).first()
session.delete(temp)
session.commit()
os.remove(os.path.join(UPLOAD_FOLDER, files[user_input]))
session.close()

print("ГОТОВО")