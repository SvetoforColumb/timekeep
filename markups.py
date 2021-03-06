from telebot import types
import dbworker


def getRemoveMarkup():
    return types.ReplyKeyboardRemove()


def getMainMarkup():
    markup_main = types.ReplyKeyboardMarkup(True)
    markup_main.row('Make a note')
    markup_main.row('View notes')
    return markup_main


def getYesNoMarkup():
    yes_no_markup = types.InlineKeyboardMarkup(row_width=2)
    yes_no_markup_row = [
        types.InlineKeyboardButton('No', callback_data="add_remind_no"),
        types.InlineKeyboardButton('Yes', callback_data="add_remind_yes")]
    yes_no_markup.row(*yes_no_markup_row)
    return yes_no_markup


def getNoteMarkup(user_id, note_id=None):
    if note_id is None:
            note_id = dbworker.getLastNotesId(user_id)
            prev_note_id = dbworker.getPrevNoteId(note_id)[0][0]
            if prev_note_id == '-':
                    note_markup = types.InlineKeyboardMarkup(row_width=2)
                    note_markup_row = [
                            types.InlineKeyboardButton('Delete', callback_data="delete_note-" + str(note_id))]
                    note_markup.row(*note_markup_row)
                    return note_markup
    else:
            prev_note_id = dbworker.getPrevNoteId(note_id)[0][0]
            if prev_note_id == '-':
                    note_markup = types.InlineKeyboardMarkup(row_width=2)
                    note_markup_row = [
                            types.InlineKeyboardButton('Delete', callback_data="delete_note-" + str(note_id))]
                    note_markup.row(*note_markup_row)
                    return note_markup
    note_markup = types.InlineKeyboardMarkup(row_width=2)
    note_markup_row = [
        types.InlineKeyboardButton('<', callback_data="prev_note-" + str(prev_note_id)),
        types.InlineKeyboardButton('Delete', callback_data="delete_note-" + str(note_id))]
    note_markup.row(*note_markup_row)
    return note_markup
