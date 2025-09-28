from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


Reply1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2"), KeyboardButton(text="Button 3")],
    [KeyboardButton(text="Location", request_location=True), KeyboardButton(text="Contact", request_contact=True)],],
    resize_keyboard=True,
    input_field_placeholder="Bitta tugmani tanlang!"
)


# Bir qatorda 10 ta tugma bo‘ladigan qilib yaratamiz
# # Bo‘sh ro‘yxat tayyorlaymiz
# buttons = []

# # for orqali 1 dan 10 gacha tugmalar yaratamiz
# for i in range(1, 11):
#     tugma = KeyboardButton(text=f"Tugma {i}")
#     buttons.append(tugma)

# # 1 qatorga joylash uchun [buttons]
# Reply2 = ReplyKeyboardMarkup(
#     keyboard=[buttons],  # faqat bitta qator
#     resize_keyboard=True
# )


# Har qatorda 2 tadan tugma bo‘ladigan qilib yaratamiz
# rows = []   # barcha qatorlar
# row = []    # vaqtinchalik qator

# for i in range(1, 11):  # 1 dan 10 gacha
#     row.append(KeyboardButton(text=f"Tugma {i}"))  # Tugma qo‘shamiz
#     if len(row) == 2:   # agar 2 ta bo‘lsa -> yangi qator
#         rows.append(row)
#         row = []        # yangi qator uchun bo‘shatamiz

# if row:  # agar oxirida tugma qolsa
#     rows.append(row)

# Reply2 = ReplyKeyboardMarkup(
#     keyboard=rows,
#     resize_keyboard=True
# )