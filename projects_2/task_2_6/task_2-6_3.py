donor_blood_type = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood_type = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()

if donor_blood_type == recipient_blood_type:
    print("Переливание возможно: группа крови донора соответствует группе крови реципиента.")
elif donor_blood_type == "I":
    print("Переливание возможно: I группа крови (0 в системе AB0) может быть перелита всем.")
elif recipient_blood_type == "I":
    print("Переливание невозможно: I группа крови (0 в системе AB0) реципиента может принимать только свою группу.")
else:
    print("Переливание невозможно: группы крови не совместимы.")


