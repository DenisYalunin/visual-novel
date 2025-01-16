define dm = Character('Дмитрий Константинович', color="#4A90E2")
define sa = Character('Саша', color="#FFF59D")
define de = Character('Денис', color="#F44336")
define al = Character('Инженер Алексей', color="#FFC107")

label start:
    scene bg_dmitriys_room with fade
    show dmitriy at left
    
    dm "Эта программа, конечно, чудо инженерной мысли. Ещё пару лет назад казалось невозможным, чтобы искусственный интеллект мог так точно анализировать каждого ученика."
    dm "Прогнозы, отчёты, даже советы для учителей… Всё это звучит прекрасно."
    dm "Но что-то здесь не так. Слишком уж жёсткие оценки она ставит некоторым детям."
    dm "Может, попробовать разобраться? Хотя я вроде бы и не программист, но понять, как она выбирает худших, мне точно под силу."
    
    hide dmitriy with fade

    scene bg_display with fade

    
    return

