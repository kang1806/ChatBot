mongoexport --db chatbot --collection training --out output.json
call activate chat
python filtering.py
python trainTraining.py
