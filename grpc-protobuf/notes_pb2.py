# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notes.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnotes.proto\x12\x05notes\"2\n\x04Note\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\x14\n\x06NoteId\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x08NoteList\x12\x1a\n\x05notes\x18\x01 \x03(\x0b\x32\x0b.notes.Note\"\x07\n\x05\x45mpty\"?\n\x11UpdateNoteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2\xdd\x01\n\x0cNotesService\x12&\n\nCreateNote\x12\x0b.notes.Note\x1a\x0b.notes.Note\x12%\n\x07GetNote\x12\r.notes.NoteId\x1a\x0b.notes.Note\x12&\n\nUpdateNote\x12\x0b.notes.Note\x1a\x0b.notes.Note\x12(\n\nDeleteNote\x12\r.notes.NoteId\x1a\x0b.notes.Note\x12,\n\x0bGetAllNotes\x12\x0c.notes.Empty\x1a\x0f.notes.NoteListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notes_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTE._serialized_start=22
  _NOTE._serialized_end=72
  _NOTEID._serialized_start=74
  _NOTEID._serialized_end=94
  _NOTELIST._serialized_start=96
  _NOTELIST._serialized_end=134
  _EMPTY._serialized_start=136
  _EMPTY._serialized_end=143
  _UPDATENOTEREQUEST._serialized_start=145
  _UPDATENOTEREQUEST._serialized_end=208
  _NOTESSERVICE._serialized_start=211
  _NOTESSERVICE._serialized_end=432
# @@protoc_insertion_point(module_scope)
