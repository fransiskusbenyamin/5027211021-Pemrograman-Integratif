import grpc
from concurrent import futures
import mysql.connector
import notes_pb2
import notes_pb2_grpc

class NotesServicer(notes_pb2_grpc.NotesServiceServicer):
    def CreateNote(self, request, context):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="grpc-note-app"
        )
        
        cursor = db.cursor()

        # Insert the new note into the database
        query = "INSERT INTO notes (title, content) VALUES (%s, %s)"
        values = (request.title, request.content)
        cursor.execute(query, values)
        db.commit()

        # Get the auto-generated ID of the inserted note
        note_id = cursor.lastrowid

        # Return the created note with the generated ID
        return notes_pb2.Note(
            id=str(note_id),
            title=request.title,
            content=request.content
        )

    def GetNote(self, request, context):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="grpc-note-app"
        )
        
        cursor = db.cursor()

        # Retrieve the note from the database
        query = "SELECT id, title, content FROM notes WHERE id = %s"
        values = (request.id,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            # Return the retrieved note
            return notes_pb2.Note(
                id=str(result[0]),
                title=result[1],
                content=result[2]
            )
        else:
            # Return an empty note if not found
            return notes_pb2.Note()

    def UpdateNote(self, request, context):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="grpc-note-app"
        )
        
        cursor = db.cursor()

        # Update the note in the database
        query = "UPDATE notes SET title = %s, content = %s WHERE id = %s"
        values = (request.title, request.content, request.id)
        cursor.execute(query, values)
        db.commit()

        # Return the updated note
        return notes_pb2.Note(
            id=request.id,
            title=request.title,
            content=request.content
        )

    def DeleteNote(self, request, context):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="grpc-note-app"
        )
        
        cursor = db.cursor()

        # Delete the note from the database
        query = "DELETE FROM notes WHERE id = %s"
        values = (request.id,)
        cursor.execute(query, values)
        db.commit()

        # Return the deleted note
        return notes_pb2.Note(
            id=request.id,
            title="",
            content=""
        )

    def GetAllNotes(self, request, context):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="grpc-note-app"
        )
        
        cursor = db.cursor()

        # Retrieve all notes from the database
        query = "SELECT id, title, content FROM notes"
        cursor.execute(query)
        results = cursor.fetchall()

        # Create a NoteList message with all notes
        note_list = notes_pb2.NoteList()
        for result in results:
            note = note_list.notes.add()
            note.id = str(result[0])
            note.title = result[1]
            note.content = result[2]

        # Return the list of notes
        return note_list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_pb2_grpc.add_NotesServiceServicer_to_server(NotesServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
