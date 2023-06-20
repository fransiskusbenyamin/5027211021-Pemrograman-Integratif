import grpc
import notes_pb2
import notes_pb2_grpc

def print_notes(notes):
    for note in notes:
        print("Note ID:", note.id)
        print("Title:", note.title)
        print("Content:", note.content)
        print()

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = notes_pb2_grpc.NotesServiceStub(channel)

    while True:
        print("Choose an action:")
        print("1. Create a note")
        print("2. Retrieve a note by ID")
        print("3. Update a note")
        print("4. Delete a note")
        print("5. Get all notes")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            new_note = stub.CreateNote(notes_pb2.Note(
                title=title,
                content=content
            ))
            print("Created Note:")
            print("Note ID:", new_note.id)
            print("Title:", new_note.title)
            print("Content:", new_note.content)
            print()
        elif choice == "2":
            note_id = input("Enter the note ID: ")
            retrieved_note = stub.GetNote(notes_pb2.NoteId(id=note_id))
            print("Retrieved Note:")
            print("Note ID:", retrieved_note.id)
            print("Title:", retrieved_note.title)
            print("Content:", retrieved_note.content)
            print()
        elif choice == "3":
            note_id = input("Enter the note ID: ")
            title = input("Enter the updated title (leave empty to keep existing): ")
            content = input("Enter the updated content (leave empty to keep existing): ")
            update_fields = {}

            if title:
                update_fields['title'] = title
            if content:
                update_fields['content'] = content

            if not update_fields:
                print("No changes provided. Exiting update process.")
                print()
                continue

            updated_note = stub.UpdateNote(notes_pb2.UpdateNoteRequest(
                id=note_id,
                **update_fields
            ))
            print("Updated Note:")
            print("Note ID:", updated_note.id)
            print("Title:", updated_note.title)
            print("Content:", updated_note.content)
            print()
        elif choice == "4":
            note_id = input("Enter the note ID: ")
            deleted_note = stub.DeleteNote(notes_pb2.NoteId(id=note_id))
            print("Deleted Note:")
            print("Note ID:", deleted_note.id)
            print("Title:", deleted_note.title)
            print("Content:", deleted_note.content)
            print()
        elif choice == "5":
            all_notes = stub.GetAllNotes(notes_pb2.Empty())
            print("All Notes:")
            print_notes(all_notes.notes)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
