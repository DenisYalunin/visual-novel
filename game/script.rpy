define dm = Character('Дмитрий Константинович', color="#4A90E2")
define sa = Character('Саша', color="#FFF59D")
define de = Character('Денис', color="#F44336")

label start:
    # Локация: Кабинет Дмитрия
    scene bg_office with fade
    show dmitriy at left
    
    # Начальный монолог Дмитрия
    dm "Эта программа, конечно, чудо инженерной мысли. Ещё пару лет назад казалось невозможным, чтобы искусственный интеллект мог так точно анализировать каждого ученика."
    dm "Прогнозы, отчёты, даже советы для учителей… Всё это звучит прекрасно."
    dm "Но что-то здесь не так. Слишком уж жёсткие оценки она ставит некоторым детям."
    dm "Может, попробовать разобраться? Хотя я вроде бы и не программист, но понять, как она выбирает худших, мне точно под силу."
    
    # Интерфейс компьютера
    call screen computer_interface
    
    return

### Экран компьютера
screen computer_interface:
    tag menu

    # Фон — рабочий стол компьютера
    add "bg_computer"
    
    # Кнопки для папок и программ
    imagemap:
        ground "bg_computer"  # Фон
        hover "bg_computer_hover"  # Подсветка кнопок (опционально)
        
        hotspot (100, 200, 200, 100) action Call("open_diary")  # Координаты и действие
        hotspot (300, 200, 200, 100) action Call("open_presentations")
        hotspot (500, 200, 200, 100) action Call("open_ai_program")
        hotspot (700, 200, 200, 100) action Call("open_mail")

label open_diary:
    dm "Это не то, здесь мои старые материалы для уроков."
    jump start

label open_presentations:
    dm "Здесь хранятся мои презентации для занятий. Но сейчас это не важно."
    jump start

label open_ai_program:
    dm "Так, эта программа мне и нужна."
    call screen ai_interface
    return

label open_mail:
    dm "Сейчас не время проверять почту. Нужно разобраться с системой."
    jump start

### Экран ИИ-программы
screen ai_interface:
    tag menu

    # Фон — интерфейс программы ИИ
    add "bg_ai_program"  # Замените на фон интерфейса программы, если есть изображение
    
    # Кнопки для вкладок
    vbox:
        textbutton "Журнал" action Call("open_journal")
        textbutton "Настройки алгоритмов" action Call("open_settings")
        textbutton "Аналитика" action Call("open_analytics")

label open_journal:
    dm "Вот они… Саша Иванов и Денис Соколов. У обоих низкий рейтинг."
    dm "Саша — вроде бы тихий мальчик, но явно отстаёт по успеваемости. А Денис… с ним совсем другая история. Его поведение — это отдельная тема."
    
    # Игрок делает выбор
    menu:
        "Поговорить с Сашей, а потом с Денисом.":
            jump talk_sasha_first
        "Поговорить с Денисом, а потом с Сашей.":
            jump talk_denis_first
        "Изучить алгоритмы программы.":
            jump study_algorithms

label open_settings:
    dm "Это настройки алгоритмов... сюда я загляну позже. Сейчас главное — найти детей, которые испытывают трудности."
    jump open_ai_program

label open_analytics:
    dm "Аналитика, конечно, полезна, но мне нужны конкретные фамилии. Пожалуй, вернусь в 'Журнал'."
    jump open_ai_program

### Продолжение: работа с учениками или алгоритмами
label talk_sasha_first:
    dm "Я думаю, начну с Саши. Нужно понять, что его так подавляет."
    # Следующая сцена с Сашей
    return

label talk_denis_first:
    dm "С Денисом будет сложнее, но это тоже важно. Начну с него."
    # Следующая сцена с Денисом
    return

label study_algorithms:
    dm "Нет, я не могу действовать наугад. Нужно понять, как работает система. Иначе я рискую сделать неверные выводы."
    # Добавить исследование алгоритмов
    return