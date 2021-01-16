from random import choice
import sys

RESULT = ""
MENU = ""
N = ""
MENU_BACKON = ""
MENU_POLIBIA = ""
MENU_POLIBIA_N = ""
main_menu = ""
alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,*%$<-?@!)(+\/|[]{}№:=1234567890"
alfavit_D = "А:ШмзЛцжРЪ!8/СшЦФ]$2нйМ)Ю*в[1№е3о|.ыюЭъ,И5аОТфэВПи9?ЩНЬЫтс+п+(}чБЯЕ@Йя\_=4ьщ{лх-гЁ7кЗдКрУбХу6%ГёДЧЖ0"
alf_bacon = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,*%$<-?@!)(+\/|[]{}№:=1234567890"
alfavit1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,"
alfavit2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_,"
alf1 = ""
alf2 = ""
mat = []
key = []
mat1 = []
mat2 = []
YOU1 = "*%$<-?@!)(+\/|[]{}№:="
YOU2 = "1234567890"
bacon_alf = ["AAAAAA","AAAAAB","AAAABA","AAAABB","AAABAA","AAABAB","AAABBA","AAABBB","AABAAB","AABABA","AABABB","AABBAA","AABBAB",
             "AABBBA","AABBBB","ABAAAA","ABAAAB","ABAABA","ABAABB","ABABAA","ABABAB","ABABBA","ABABBB","ABBAAA","ABBAAB","ABBABA",
             "ABBABB","ABBBAA","ABBBAB","ABBBBA","ABBBBB","BAAAAA","BAAAAB","BAAABA","BAAABB","BAABAA","BAABAB","BAABBA","BAABBB",
             "BABAAA","BABAAB","BABABA","BABABB","BABBAA","BABBAB","BABBBA","BABBBB","BBAAAA","BBAAAB","BBAABA","BBAABB","BBABAA",
             "BBABAB","BBABBA","BBABBB","BBBAAA","BBBAAB","BBBABA","BBBABB","BBBBAA","BBBBAB","BBBBBA","BBBBBB","АААААА","АААААВ",
             "ААААВА","ААААВВ","АААВАА","АААВАВ","АААВВА","АААВВВ","ААВААА","ААВААВ","ААВАВА","ААВАВВ","ААВВАА","ААВВАВ","ААВВВА",
             "ААВВВВ","АВАААА","АВАААВ","АВААВА","АВААВВ","АВАВАА","АВАВАВ","АВАВВА","АВАВВВ","АВВААА","АВВААВ","АВВАВА","АВВАВВ",
             "АВВВАА","АВВВАВ","АВВВВА","АВВВВВ","ВААААА","ВААААВ","ВАААВА","ВАААВВ","BBBBBB"]
def obrabotka(k):
    '''функция обрабатывает ключ, убирает ненужные символы (повторяющиеся в слове)'''
    key = []
    for let in k:
        if let not in key:
            key.append(let)
    key = "".join(key)
    return key

def normalise(mes,alf):
    '''принимает строку, переводит в нижний регистр, удаляет симфолы, которых нет в условии'''
    pr = ""
    for let in mes:
        if let in alf:
            pr += let
    return pr

def keyboard(k,alf):
    k = normalise(k,alfavit)
    k = obrabotka(k)
    for key in k:
        if key in alf:
            if alf.index(key) == len(alf):
                alf = alf[:alf.index(key)]
            else:
                alf = alf[:alf.index(key)] + alf[alf.index(key) + 1:]
                global alf1
                alf1 = k + alf
    return alf1

def chetnie(alfavit):
    '''составление букв с четными символами (B - формат)'''
    chet = []
    i = 1
    while i < len(alfavit):
        chet.append(alfavit[i])
        i += 2
    return chet

def nechetnie(alfavit):
    '''составление букв с нечетными символами (A - формат)'''
    nechet = []
    i = 0
    while i < len(alfavit):
        nechet.append(alfavit[i])
        i += 2
    return nechet

def kluch(k):
    '''функция определяет последовательность ключа для шифрования/дешифрования'''
    key = []
    for let in k:
        if let not in key:
            key.append(let)
    key.sort()
    key = "".join(key)
    return key
    
def sozdanie(k,m):
    '''ФУНКИЦИЯ СОЗДАЁТ СРЕДУ КЛЮЧА ДЛЯ ШИФРОВАНИЯ'''
    global S
    if len(m)%len(k) == 0:
        S = (k*(len(m)//len(k)))[0:len(m)]
    else:
        S = (k*((len(m)//len(k))+1))[0:len(m)]
    return ""

def random(blocknoteCrypt,blocknoteEncrypt):
    '''функция генерирует рандомный словарь'''
    import os.path
    if (os.path.isfile(blocknoteCrypt) and os.path.isfile(blocknoteEncrypt)) == True:
        f = open(blocknoteCrypt,"r")
        r = open(blocknoteEncrypt,"r")
    else:
        import random
        import shutil
        f = open(blocknoteCrypt,"w")
        for i in range(1000):
            f.write(random.choice(alfavit))
        f.close()
        r = shutil.copy(blocknoteCrypt,blocknoteEncrypt)
        f = open(blocknoteCrypt,"r")
        r = open(blocknoteEncrypt,"r")
        f.close()
        r.close()
    return ""

def obrabotka_txt(N,m,blocknoteCrypt,blocknoteEncrypt):
    '''Обрабатывает txt документ - удаляет из словаря ненужные файлы'''
    if N == "1":
        f = open(blocknoteCrypt,"w+")
        r = open(blocknoteEncrypt,"r")
        s = r.read()[len(m)::]
        f.write(s)
        f.close()
        r.close()
        f = open(blocknoteCrypt,"r")
        f.read()
        return ""
    elif N == "2":
        r = open(blocknoteEncrypt,"w+")
        f = open(blocknoteCrypt,"r")
        s = f.read()
        r.write(s)
        r.close()
        f.close()
        r = open(blocknoteCrypt,"r")
        r.read()
        return ""
    else:
        return ""
def matrix1(m,k):
    '''создание специальной матрицы 1'''
    global S
    if len(m)%k == 0:
        S = len(m)/k
    else:
        S = ((len(m)/k)+1)
    global mat
    mat = [["."] * (int(S)) for _ in range(k)]
    try:
        r = 0
        for i in range(int(S)):
            for j in range(k):
                mat[j][i] = m[r]
                r += 1
        return ""
    except IndexError:
        return ""

def matrix2(m,k):
    '''создание специальной матрицы 2'''
    global S
    if len(m)%k == 0:
        S = len(m)/k
    else:
        S = ((len(m)/k)+1)
    global mat
    mat = [["."] * (int(S)) for _ in range(k)]
    try:
        r = 0
        for i in range(k):
            for j in range(int(S)):
                mat[i][j] = m[r]
                r += 1
        return ""
    except IndexError:
        return ""

def matrix_1(m,k):
    '''создание специальной матрицы _1'''
    global S
    if len(m)%len(k) == 0:
        S = len(m)/len(k)
    else:
        S = ((len(m)/len(k)+1))
    global mat
    mat = [["."] * (len(k)) for _ in range(int(S))]
    try:
        r = 0
        for i in range(int(S)):
            for j in range(len(k)):
                mat[i][j] = m[r]
                r += 1
        return ""
    except IndexError:
        return ""
    
def matrix_2(m,k):
    '''создание специальной матрицы _2'''
    global S
    if len(m)%len(k) == 0:
        S = len(m)/len(k)
    else:
        S = ((len(m)/len(k)+1))
    global mat
    mat = [["."] * (len(k)) for _ in range(int(S))]
    try:
        r = 0
        for i in range(len(k)):
            for j in range(int(S)):
                mat[j][i] = m[r]
                r += 1
        return ""
    except IndexError:
        return ""
    
def _matrix_(alf):
    '''функция создаёт матрицу с помощью алфавита'''
    mat = [["."] * (10) for _ in range(10)]
    try:
        r = 0
        for i in range(10):
            for j in range(10):
                mat[i][j] = alf[r]
                r += 1
        return mat
    except IndexError:
        return ""

class A1: 
    def _encrypt_сeasar(m,k):
        '''шифрует сообщение(m) ключом(k)'''
        global RESULT
        m = normalise(m,alfavit)
        result = ""
        for let in m:
            result += alfavit[(alfavit.index(let)+k)%len(alfavit)]
        RESULT = result
        return result   
    def _decrypt_сeasar(c,k):
        '''дешифрует зашифрованное сообщение(c) ключом(k)'''
        global RESULT
        result = A1._encrypt_сeasar(c,(len(alfavit)-k))
        RESULT = result
        return result 
    def _encrypt_decrypt_atbash(m):
        '''шифрует/дешифрует сообщение(m,c) ключом(k)'''
        global RESULT
        m = normalise(m,alfavit) 
        result = ""
        for let in m:
            result += alfavit[len(alfavit) - alfavit.index(let) - 1]
        RESULT = result
        return result   
    def _encrypt_zamena(m):
        global RESULT
        m = normalise(m,alfavit) 
        result = ""
        for let in m:
            result += alfavit_D[alfavit.index(let)]
        RESULT = result
        return result
    def _decrypt_zamena(c):
        global RESULT
        c = normalise(c,alfavit)
        result = ""
        for let in c:
            result += alfavit[alfavit_D.index(let)]
        RESULT = result
        return result
    def _encrypt_zamena_kodovoe_slovo(m,k):
        '''шифрует сообщение(m) ключом(k)'''
        global RESULT
        alf1 = keyboard(k,alfavit)
        m = normalise(m,alfavit)
        result = ""
        for let in m:
            result += alf1[alfavit.index(let)]
        RESULT = result
        return result
    def _decrypt_zamena_kodovoe_slovo(c,k):
        '''шифрует сообщение(m) ключом(k)'''
        global RESULT
        alf1 = keyboard(k,alfavit)
        c = normalise(c,alfavit)
        result = ""
        for let in c:
            result += alfavit[alf1.index(let)]
        RESULT = result
        return result
    def _1_bacon_encrypt(m):
        '''Функция шифрования 1 МЕТОДОМ БЭКОНА (МЕТОД ПРОСТОЙ ЗАМЕНЫ)'''
        m = normalise(m,alfavit) 
        global RESULT
        result = ""
        for i in range(len(m)):
            result += bacon_alf[alf_bacon.index(m[i])]
        RESULT = result
        return result
    def _1_bacon_decrypt(c):
        '''Функция дешифрования 1 МЕТОДОМ БЭКОНА (МЕТОД ПРОСТОЙ ЗАМЕНЫ)'''
        global RESULT
        result = ""
        i = 0
        while i < len(c):
            result += alf_bacon[bacon_alf.index(c[i:(i + len(bacon_alf[0]))])]
            i += len(bacon_alf[0])
        RESULT = result
        return result
    def _2_bacon_encrypt(m):
        '''Функция шифрования 2 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ РЕГИСТР БУКВ )'''
        global RESULT
        result = ""
        m = A1._1_bacon_encrypt(m)
        for i in range(len(m)):
            if m[i] == "А":
                result += choice(YOU1)
            elif m[i] == "В":
                result += choice(YOU2)
            elif m[i] == "A":
                result += choice(alf_bacon[33:-36])
            elif m[i] == "B":
                result += choice(alf_bacon[:-69])
        RESULT = result
        return result
    def _2_bacon_decrypt(c):
        '''Функция дешифрования 2 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ РЕГИСТР БУКВ )'''
        global RESULT
        result = ""
        for i in range(len(c)):
            if c[i] in YOU1:
                result += "А"
            elif c[i] in YOU2:
                result += "В"
            elif c[i] in alf_bacon[33:-36]:
                result += "A"
            elif c[i] in alf_bacon[:-69]:
                result += "B"
        if len(result) % len(bacon_alf[0]) > 0:
            result = result[:(len(result) // len(bacon_alf[0]) * len(bacon_alf[0]))]
        result = A1._1_bacon_decrypt(result)
        RESULT = result
        return result
    def _3_bacon_encrypt(m, glas = "аеиоуыэюя", soglas = "бвгджзйклмнпрстфхцчшщъь"):
        '''Функция шифрования 3 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ГЛАСНЫЕ И СОГЛАСНЫЕ )'''
        global RESULT
        result = ""
        m = A1._1_bacon_encrypt(m)
        for i in range(len(m)):
            if m[i] == "А":
                result += choice(YOU1)
            elif m[i] == "В":
                result += choice(YOU2)
            elif m[i] == "A":
                result += choice(glas)
            elif m[i] == "B":
                result += choice(soglas)
        RESULT = result
        return result
    def _3_bacon_decrypt(c, glas = "аеиоуыэюя", soglas = "бвгджзйклмнпрстфхцчшщъь"):
        '''Функция дешифрования 3 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ГЛАСНЫЕ И СОГЛАСНЫЕ )'''
        global RESULT
        result = ""
        for i in range(len(c)):
            if c[i] in YOU1:
                result += "А"
            elif c[i] in YOU2:
                result += "В"
            elif c[i] in glas:
                result += "A"
            elif c[i] in soglas:
                result += "B"
        result = A1._1_bacon_decrypt(result)
        RESULT = result
        return result
    def _4_bacon_encrypt(m):
        '''Функция шифрования 4 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПРИНАДЛЕЖНОСТЬ К ЧАСТЯМ АЛФАВИТА )'''
        global RESULT
        result = ""
        m = A1._1_bacon_encrypt(m)
        for i in range(len(m)):
            if m[i] == "А":
                result += choice(alf_bacon[64:82])
            elif m[i] == "В":
                result += choice(alf_bacon[82:])
            elif m[i] == "A":
                result += choice(alf_bacon[:32])
            elif m[i] == "B":
                result += choice(alf_bacon[32:64])
        RESULT = result
        return result
    def _4_bacon_decrypt(c):
        '''Функция дешифрования 4 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПРИНАДЛЕЖНОСТЬ К ЧАСТЯМ АЛФАВИТА )'''
        global RESULT
        result = ""
        for i in range(len(c)):
            if c[i] in alf_bacon[64:82]:
                result += "А"
            elif c[i] in alf_bacon[82:]:
                result += "В"
            elif c[i] in alf_bacon[:32]:
                result += "A"
            elif c[i] in alf_bacon[32:64]:
                result += "B"
        result = A1._1_bacon_decrypt(result)
        RESULT = result
        return result
    def _5_bacon_encrypt(m):
        '''Функция шифрования 5 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПОРЯДКОВЫЙ НОМЕР БУКВЫ (ЧЕТНЫЙ/НЕЧЕТНЫЙ) )'''
        global RESULT
        result = ""
        m = A1._1_bacon_encrypt(m)
        for i in range(len(m)):
            if m[i] == "А":
                result += choice(nechetnie(alfavit[64:]))
            elif m[i] == "В":
                result += choice(chetnie(alfavit[64:]))
            elif m[i] == "A":
                result += choice(nechetnie(alfavit[:-36]))
            elif m[i] == "B":
                result += choice(chetnie(alfavit[:-36]))
        RESULT = result
        return result
    def _5_bacon_decrypt(c):
        '''Функция дешифрования 5 МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПОРЯДКОВЫЙ НОМЕР БУКВЫ (ЧЕТНЫЙ/НЕЧЕТНЫЙ) )'''
        global RESULT
        result = ""
        chet_ = chetnie(alfavit[64:])
        nechet_ = nechetnie(alfavit[64:])
        chet = chetnie(alfavit[:-36])
        nechet = nechetnie(alfavit[:-36])
        for i in range(len(c)):
            if c[i] in nechet_:
                result += "А"
            elif c[i] in chet_:
                result += "В"
            elif c[i] in nechet:
                result += "A"
            elif c[i] in chet:
                result += "B"
        result = A1._1_bacon_decrypt(result)
        RESULT = result
        return result
    def _encrypt_vidjiner(m,k):
        global RESULT
        m = normalise(m,alfavit)
        k = obrabotka(k)
        N = sozdanie(k,m)
        result = ""
        for i in range(len(S)):
            if (alfavit.index(m[i]) + alfavit.index(S[i]) < len(alfavit)):
                result += alfavit[(alfavit.index(m[i]) + alfavit.index(S[i]))]
            elif (alfavit.index(m[i]) + alfavit.index(S[i])) >= len(alfavit):
                result += alfavit[((alfavit.index(m[i]) + alfavit.index(S[i]))%len(alfavit))]
        RESULT = result
        return result
    def _decrypt_vidjiner(c,k):
        global RESULT
        k = obrabotka(k)
        key = kluch(k)
        N = sozdanie(k,c)
        result = ""
        for i in range(len(S)):
            if (alfavit.index(c[i]) + (len(alfavit) - alfavit.index(S[i])) < len(alfavit)):
                result += alfavit[(alfavit.index(c[i]) + (len(alfavit) - alfavit.index(S[i])))]
            elif (alfavit.index(c[i]) + (len(alfavit) - alfavit.index(S[i]))) >= len(alfavit):
                result += alfavit[((alfavit.index(c[i]) + (len(alfavit) - alfavit.index(S[i])))%len(alfavit))]
        result = normalise(result,alfavit)
        RESULT = result
        return result
    def _encrypt_blocknote(m,b1,b2):
        global RESULT
        m = normalise(m,alfavit)
        random(b1,b2)
        result = ""
        for i in range(len(m)):
            f = open(b1,"r")
            s = f.read()
            result += alfavit[(alfavit.index(m[i])+alfavit.index(s[i]) + 1)%(len(alfavit)-1)]  
        obrabotka_txt(N,m,b1,b2)
        RESULT = result
        return result
    def _decrypt_blocknote(c,b1,b2):
        global RESULT
        c = normalise(c,alfavit)
        random(b1,b2)
        result = ""
        for i in range(len(c)):
            r = open(b2,"r")
            s = r.read()
            result += alfavit[(alfavit.index(c[i])+((len(alfavit)-1) - alfavit.index(s[i])) - 1)%(len(alfavit)-1)]  
        obrabotka_txt(N,c,b1,b2)
        RESULT = result
        return result

def _1_METHOD_BACON(MENU_BACKON):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) 1-ым МЕТОДОМ БЭКОНА ( МЕТОД ПРОСТОЙ ЗАМЕНЫ )'''
    print()
    print("╔══════════════════════════════╗")
    print("║     МЕТОД ПРОСТОЙ ЗАМЕНЫ     ║")
    print("║══════════════════════════════║")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝")
    print()
    global N
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_METHOD_BACON(MENU_BACKON)
        A1._1_bacon_encrypt(m)
        print()
        print("ВАШ ТЕКСТ: ",A1._1_bacon_encrypt(m))
        print()
        input("Нажмите Enter для продолжения...")
        _1_METHOD_BACON(MENU_BACKON)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ЗАКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_METHOD_BACON(MENU_BACKON)
        A1._1_bacon_decrypt(c)
        print()
        print("ВАШ ТЕКСТ: ",A1._1_bacon_decrypt(c))
        print()
        input("Нажмите Enter для продолжения...")
        _1_METHOD_BACON(MENU_BACKON)
    elif N == "*":
            print()
            print("OK!")
            A(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _1_METHOD_BACON(MENU_BACKON)
    return ""

def _2_METHOD_BACON(MENU_BACKON):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) 2-ым МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ РЕГИСТР БУКВ )'''
    print()
    print("╔══════════════════════════════╗")
    print("║   ЗАМЕНА ЧЕРЕЗ РЕГИСТР БУКВ  ║")
    print("║══════════════════════════════║")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝")
    print()
    global N
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_METHOD_BACON(MENU_BACKON)
        A1._2_bacon_encrypt(m)
        print()
        print("ВАШ ТЕКСТ: ",A1._2_bacon_encrypt(m))
        print()
        input("Нажмите Enter для продолжения...")
        _2_METHOD_BACON(MENU_BACKON)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_METHOD_BACON(MENU_BACKON)
        A1._2_bacon_decrypt(c)
        print()
        print("ВАШ ТЕКСТ: ",A1._2_bacon_decrypt(c))
        print()
        input("Нажмите Enter для продолжения...")
        _2_METHOD_BACON(MENU_BACKON)
    elif N == "*":
            print()
            print("OK!")
            A(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _2_METHOD_BACON(MENU_BACKON)
    return ""
  
def _3_METHOD_BACON(MENU_BACKON):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) 3-им МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ГЛАСНЫЕ И СОГЛАСНЫЕ )'''
    print()
    print("╔══════════════════════════════╗")
    print("║  ЗАМЕНА ЧЕРЕЗ ГЛАСН/СОГЛАСН  ║")
    print("║══════════════════════════════║")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝") 
    print()
    global N
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_METHOD_BACON(MENU_BACKON)
        A1._3_bacon_encrypt(m)
        print()
        print("ВАШ ТЕКСТ: ",A1._3_bacon_encrypt(m))
        print()
        input("Нажмите Enter для продолжения...")
        _3_METHOD_BACON(MENU_BACKON)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_METHOD_BACON(MENU_BACKON)
        A1._3_bacon_decrypt(c)
        print()
        print("ВАШ ТЕКСТ: ",A1._3_bacon_decrypt(c))
        print()
        input("Нажмите Enter для продолжения...")
        _3_METHOD_BACON(MENU_BACKON)
    elif N == "*":
            print()
            print("OK!")
            A(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _3_METHOD_BACON(MENU_BACKON)
    return ""

def _4_METHOD_BACON(MENU_BACKON):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) 4-ым МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПРИНАДЛЕЖНОСТЬ К ЧАСТЯМ АЛФАВИТА )'''
    print()
    print("╔══════════════════════════════╗")
    print("║ЗАМЕНА ПРИНАДЛЕЖНОСТЬ АЛФАВИТУ║")
    print("║══════════════════════════════║")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝")
    print()
    global N
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _4_METHOD_BACON(MENU_BACKON)
        A1._4_bacon_encrypt(m)
        print()
        print("ВАШ ТЕКСТ: ",A1._4_bacon_encrypt(m))
        print()
        input("Нажмите Enter для продолжения...")
        _4_METHOD_BACON(MENU_BACKON)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _4_METHOD_BACON(MENU_BACKON)
        A1._4_bacon_decrypt(c)
        print()
        print("ВАШ ТЕКСТ: ",A1._4_bacon_decrypt(c))
        print()
        input("Нажмите Enter для продолжения...")
        _4_METHOD_BACON(MENU_BACKON)
    elif N == "*":
            print()
            print("OK!")
            A(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _4_METHOD_BACON(MENU_BACKON)
    return ""

def _5_METHOD_BACON(MENU_BACKON):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) 5-ым МЕТОДОМ БЭКОНА ( МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПОРЯДКОВЫЙ НОМЕР БУКВЫ (ЧЕТНЫЙ/НЕЧЕТНЫЙ) )'''
    print()
    print("╔══════════════════════════════╗")
    print("║ ЗАМЕНА № БУКВЫ (ЧЕТН/НЕЧЕТН) ║")
    print("║══════════════════════════════║")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝")
    print()
    global N
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _5_METHOD_BACON(MENU_BACKON)
        A1._5_bacon_encrypt(m)
        print()
        print("ВАШ ТЕКСТ: ",A1._5_bacon_encrypt(m))
        print()
        input("Нажмите Enter для продолжения...")
        _5_METHOD_BACON(MENU_BACKON) 
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _5_METHOD_BACON(MENU_BACKON)
        A1._5_bacon_decrypt(c)
        print()
        print("ВАШ ТЕКСТ: ",A1._5_bacon_decrypt(c))
        print()
        input("Нажмите Enter для продолжения...")
        _5_METHOD_BACON(MENU_BACKON)
    elif N == "*":
            print()
            print("OK!")
            A(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _5_METHOD_BACON(MENU_BACKON)
    return ""

def A(MENU):
    '''МЕНЮ ВЫПОЛНЕНИЯ ПОДСТАНОВОНЫХ ШИФРОВ'''
    global N
    if MENU == "1":
        print()
        print("╔══════════════════════════════╗")
        print("║          ШИФР ЦЕЗАРЯ         ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = int(input("ВВЕДИТЕ КЛЮЧ (ЦИФРА): "))
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_сeasar(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = int(input("ВВЕДИТЕ КЛЮЧ (ЦИФРА): "))
            print()
            print("ВАШ ТЕКСТ: ",A1._decrypt_сeasar(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
            
    elif MENU == "2":
        print()
        print("╔══════════════════════════════╗")
        print("║           ШИФР АТБАШ         ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_decrypt_atbash(m))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_decrypt_atbash(m))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        return ""
    
    elif MENU == "3":
        print()
        print("╔══════════════════════════════╗")
        print("║          ШИФР ЗАМЕНЫ         ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_zamena(m))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print()
            print("ВАШ ТЕКСТ: ",A1._decrypt_zamena(c))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        return ""
    
    elif MENU == "4":
        print()
        print("╔══════════════════════════════╗")
        print("║ ШИФР ЗАМЕНЫ С КОДОВЫМ СЛОВОМ ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_zamena_kodovoe_slovo(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",A1._decrypt_zamena_kodovoe_slovo(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        return ""
    elif MENU == "5":
        '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) МЕТОДАМИ БЭКОНА'''
        print()
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                           ШИФР БЭКОНА                             ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 1 --- МЕТОД ПРОСТОЙ ЗАМЕНЫ                                        ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 2 --- МЕТОД ЗАМЕНЫ ЧЕРЕЗ РЕГИСТР БУКВ                             ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 3 --- МЕТОД ЗАМЕНЫ ЧЕРЕЗ ГЛАСНЫЕ И СОГЛАСНЫЕ                      ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 4 --- МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПРИНАДЛЕЖНОСТЬ К ЧАСТЯМ АЛФАВИТА         ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 5 --- МЕТОД ЗАМЕНЫ ЧЕРЕЗ ПОРЯДКОВЫЙ НОМЕР БУКВЫ (ЧЕТНЫЙ/НЕЧЕТНЫЙ) ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")    
        print()
        global MENU_BACKON
        MENU_BACKON = input("ВАШ ВЫБОР: ")
        if MENU_BACKON == "1":
            _1_METHOD_BACON(MENU_BACKON)
        elif MENU_BACKON == "2":
            _2_METHOD_BACON(MENU_BACKON)
        elif MENU_BACKON == "3":
            _3_METHOD_BACON(MENU_BACKON)
        elif MENU_BACKON == "4":
            _4_METHOD_BACON(MENU_BACKON)
        elif MENU_BACKON == "5":
            _5_METHOD_BACON(MENU_BACKON)
        elif MENU_BACKON == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        return ""
    
    elif MENU == "6":
        print()
        print("╔══════════════════════════════╗")
        print("║        ШИФР ВИЖЕНЕРА         ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",A1._encrypt_vidjiner(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",A1._decrypt_vidjiner(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...") 
            A(MENU)
        return ""

    elif MENU == "7":
        print()
        print("╔══════════════════════════════╗")
        print("║        ШИФР ВЕРНАМА          ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            blocknoteCrypt = input("Введите название блокнота шифрования: ") + ".txt"
            blocknoteEncrypt = input("Введите название блокнота дешифрования: ") + ".txt"
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print("ВАШ ТЕКСТ: ",A1._encrypt_blocknote(m,blocknoteCrypt,blocknoteEncrypt))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "2":
            blocknoteCrypt = input("Введите название блокнота шифрования: ") + ".txt"
            blocknoteEncrypt = input("Введите название блокнота дешифрования: ") + ".txt"
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                A(MENU)
            print("ВАШ ТЕКСТ: ",A1._decrypt_blocknote(c,blocknoteCrypt,blocknoteEncrypt))
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_A(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            A(MENU)
        return ""
    
class B1: 
    def _encrypt_skitala(m,k):
        global RESULT
        m = normalise(m,alfavit)
        rey = ""
        matrix1(m,k)
        result = ""
        for n in range(k):
            for s in range(int(S)):
                result += mat[n][s]
        RESULT = result
        return result
    def _decrypt_skitala(c,k):
        global RESULT
        matrix2(c,k)
        result = ""
        for n in range(int(S)):
            for s in range(k):
                result += mat[s][n]
        result = normalise(result,alfavit)
        RESULT = result
        return result
 
    def _encrypt_perestanovka(m,k):
        '''шифрует сообщение(m) ключом(k)'''
        global RESULT
        alf1 = keyboard(k,alfavit)
        m = normalise(m,alfavit)
        result = ""
        for let in m:
            result += alf1[alfavit.index(let)]
        RESULT = result
        return result
    def _decrypt_perestanovka(c,k):
        '''шифрует сообщение(c) ключом(k)'''
        global RESULT
        alf1 = keyboard(k,alfavit)
        c = normalise(c,alfavit)
        result = ""
        for let in c:
            result += alfavit[alf1.index(let)]
        RESULT = result
        return result

    def _encrypt_perestanovka_s_kluchom(m,k):
        global RESULT
        m = normalise(m,alfavit)
        k = obrabotka(k)
        key = kluch(k)
        matrix_1(m,k)
        result = ""
        for n in range(len(k)):
            for s in range(int(S)):
                result += mat[s][k.index(key[n])]
        RESULT = result
        return result
    def _decrypt_perestanovka_s_kluchom(c,k):
        global RESULT
        c = normalise(c,alfavit)
        k = obrabotka(k)
        key = kluch(k)
        matrix_2(c,k)
        result = ""
        result1 = ""
        for n in range(int(S)):
            for s in range(len(k) ):
                result += mat[n][key.index(k[s])]
        result = normalise(result,alfavit)
        RESULT = result
        return result

def B(MENU):
    '''МЕНЮ ВЫПОЛНЕНИЯ ПЕРЕСТАНОВОЧНЫХ ШИФРОВ'''
    if MENU == "1":
        print()
        print("╔══════════════════════════════╗")
        print("║         ШИФР «СКИТАЛА»       ║")
        print("╠══════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = int(input("ВВЕДИТЕ КЛЮЧ (ЦИФРА): "))
            print()
            print("ВАШ ТЕКСТ: ",B1._encrypt_skitala(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = int(input("ВВЕДИТЕ КЛЮЧ (ЦИФРА): "))
            print()
            print("ВАШ ТЕКСТ: ",B1._decrypt_skitala(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_B(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
            
    elif MENU == "2":
        print()
        print("╔═════════════════════════════════════════╗")
        print("║ ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ             ║")
        print("╠═════════════════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ            ║")
        print("╠═════════════════════════════════════════╣")
        print("║ * --- НАЗАД                             ║")
        print("╚═════════════════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._encrypt_perestanovka(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._decrypt_perestanovka(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_B(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        return ""
    
    elif MENU == "3":
        print()
        print("╔══════════════════════════════════════════════════╗")
        print("║ ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР С КЛЮЧОМ ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                      ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                     ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                      ║")
        print("╚══════════════════════════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (ЧИСЛО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._encrypt_perestanovka_s_kluchom(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (ЧИСЛО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._decrypt_perestanovka_s_kluchom(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_B(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        return ""
    
    elif MENU == "4":
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║ ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР С КОДОВЫМ СЛОВОМ ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                              ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                             ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                              ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._encrypt_perestanovka_s_kluchom(m,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                B(MENU)
            k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",B1._decrypt_perestanovka_s_kluchom(c,k))
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_B(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            B(MENU)
        return ""
class C1:
    def _1_encrypt_method_kvadrat_polobia(m,k):
        global RESULT
        m = normalise(m,alfavit)
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alfavit.index(m[n])%10] == m[n]:
                    result += mat[(s+1)%10][alfavit.index(m[n])%10]
        RESULT = result
        return result
    def _1_decrypt_method_kvadrat_polobia(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alfavit.index(c[n])%10] == c[n]:
                    result += mat[(s-1)%10][alfavit.index(c[n])%10]
        result = normalise(result,alfavit)
        RESULT = result
        return result
  
    def _1_encrypt_method_kvadrat_polobia_kluch(m,k):
        global RESULT
        m = normalise(m,alfavit)
        keyboard(k,alfavit)
        mat = _matrix_(alf1) 
        result = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alf1.index(m[n])%10] == m[n]:
                    result += mat[(s+1)%10][alf1.index(m[n])%10]
        RESULT = result
        return result
    def _1_decrypt_method_kvadrat_polobia_kluch(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alf1)
        result = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alf1.index(c[n])%10] == c[n]:
                    result += mat[(s-1)%10][alf1.index(c[n])%10]
        result = normalise(result,alfavit)
        RESULT = result
        return result

    def _2_encrypt_method_kvadrat_polobia(m,k):
        global RESULT
        m = normalise(m,alfavit)
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        result1 = ""
        res1 = ""
        res2 = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alfavit.index(m[n])%10] == m[n]:
                    res1 += str(alfavit.index(m[n])%10)
                    res2 += str(s)
        result1 = res2 + res1
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result
    def _2_decrypt_method_kvadrat_polobia(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        result1 = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alfavit.index(c[n])%10] == c[n]:
                    result1 += str(s) + str(alfavit.index(c[n])%10)
        n = 0
        while n <= ((len(result1)//2)-1):
            result += mat[int(result1[n])][int(result1[n+(len(result1)//2)])]
            n += 1
        RESULT = result
        return result
 
    def _2_encrypt_method_kvadrat_polobia_kluch(m,k):
        global RESULT
        m = normalise(m,alfavit)
        keyboard(k,alfavit)
        mat = _matrix_(alf1)
        result = ""
        result1 = ""
        res1 = ""
        res2 = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alf1.index(m[n])%10] == m[n]:
                    res1 += str(alf1.index(m[n])%10)
                    res2 += str(s)
        result1 = res2 + res1
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result
    def _2_decrypt_method_kvadrat_polobia_kluch(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alf1)
        result = ""
        result1 = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alf1.index(c[n])%10] == c[n]:
                    result1 += str(s) + str(alf1.index(c[n])%10)
        n = 0
        while n <= ((len(result1)//2)-1):
            result += mat[int(result1[n])][int(result1[n+(len(result1)//2)])]
            n += 1
        RESULT = result
        return result

    def _3_encrypt_method_kvadrat_polobia(m,k):
        global RESULT
        m = normalise(m,alfavit)  
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        result1 = ""
        result2 = ""
        res1 = ""
        res2 = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alfavit.index(m[n])%10] == m[n]:
                    result2 += str(s) + str(alfavit.index(m[n])%10)
        result1 = result2[1:] + result2[0]
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result
    def _3_decrypt_method_kvadrat_polobia(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alfavit)
        result = ""
        result1 = ""
        result2 = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alfavit.index(c[n])%10] == c[n]:
                    result2 += str(s) + str(alfavit.index(c[n])%10)
        result1 = result2[-1] + result2[:-1]
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result

    def _3_encrypt_method_kvadrat_polobia_kluch(m,k):
        global RESULT
        m = normalise(m,alfavit)
        keyboard(k,alfavit)
        mat = _matrix_(alf1)
        result = ""
        result1 = ""
        result2 = ""
        res1 = ""
        res2 = ""
        for n in range(len(m)):
            for s in range(10):
                if mat[s][alf1.index(m[n])%10] == m[n]:
                    result2 += str(s) + str(alf1.index(m[n])%10)
        result1 = result2[1:] + result2[0]
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result
    def _3_decrypt_method_kvadrat_polobia_kluch(c,k):
        global RESULT
        keyboard(k,alfavit)
        mat = _matrix_(alf1)
        result = ""
        result1 = ""
        result2 = ""
        for n in range(len(c)):
            for s in range(10):
                if mat[s][alf1.index(c[n])%10] == c[n]:
                    result2 += str(s) + str(alf1.index(c[n])%10)
        result1 = result2[-1] + result2[:-1]
        n = 0
        while n <= (len(result1)-1):
            result += mat[int(result1[n])][int(result1[n+1])]
            n = n + 2
        RESULT = result
        return result

    def _encrypt_4_kvadrata(m,k1,k2):
        global RESULT
        '''функция шифрования методом шифра четырёх квадратов'''
        m = normalise(m,alfavit)
        alf1 = keyboard(k1,alfavit)
        alf2 = keyboard(k2,alfavit)
        mat = _matrix_(alfavit)
        mat1 = _matrix_(alf1)
        mat2 = _matrix_(alf2)
        if len(m)%2 != 0:
            m = m[::] + "."
        result = ""
        i = 0
        while i < len(m):
            result += mat2[alfavit.index(m[i+1])//10][alfavit.index(m[i])%10]
            result += mat1[alfavit.index(m[i])//10][(alfavit.index(m[i+1])%10)]
            i += 2
        RESULT = result
        return result
    def _decrypt_4_kvadrata(c,k1,k2):
        global RESULT
        '''функция дешифрования методом шифра четырёх квадратов'''
        c = normalise(c,alfavit)
        alf1 = keyboard(k1,alfavit)
        alf2 = keyboard(k2,alfavit)
        mat = _matrix_(alfavit)
        mat1 = _matrix_(alf1)
        mat2 = _matrix_(alf2)
        if len(c)%2 != 0:
            c = c[::] + "."
        result = ""
        i = 0
        while i < len(c):
            result += mat[alf1.index(c[i+1])//10][alf2.index(c[i])%10]
            result += mat[alf2.index(c[i])//10][(alf1.index(c[i+1])%10)]
            i += 2
        result = normalise(result,alfavit)
        RESULT = result
        return result
def _1_method_polibia(MENU_POLIBIA_N):
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║            МЕТОД СДВИГА ПО СТОЛБЦАМ          ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                 ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                  ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._1_encrypt_method_kvadrat_polobia(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._1_decrypt_method_kvadrat_polobia(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _1_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_polibia(MENU_POLIBIA_N)
    return ""
def _1_method_s_kluchom_polibia(MENU_POLIBIA_N):
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║ МЕТОД СДВИГА ПО СТОЛБЦАМ (С КЛЮЧЕВЫМ СЛОВОМ) ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                 ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                  ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._1_encrypt_method_kvadrat_polobia_kluch(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._1_decrypt_method_kvadrat_polobia_kluch(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _1_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
    return ""

def _2_method_polibia(MENU_POLIBIA_N):
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║        МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК         ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                 ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                  ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._2_encrypt_method_kvadrat_polobia(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._2_decrypt_method_kvadrat_polobia(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _2_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_polibia(MENU_POLIBIA_N)
    return ""
def _2_method_s_kluchom_polibia(MENU_POLIBIA_N):
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print("║ МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК (С КЛЮЧЕВЫМ СЛОВОМ) ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                       ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                      ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                       ║")
    print("╚═══════════════════════════════════════════════════╝")
    print()
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._2_encrypt_method_kvadrat_polobia_kluch(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._2_decrypt_method_kvadrat_polobia_kluch(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _2_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
    return ""
def _3_method_polibia(MENU_POLIBIA_N):
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║        МЕТОД ЦИКЛИЧЕСКОГО СДВИГА             ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                 ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                  ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._3_encrypt_method_kvadrat_polobia(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_method_polibia(MENU_POLIBIA_N)
        k = "а"
        print()
        print("ВАШ ТЕКСТ: ",C1._3_decrypt_method_kvadrat_polobia(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _3_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_polibia(MENU_POLIBIA_N)
    return ""
def _3_method_s_kluchom_polibia(MENU_POLIBIA_N):
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print("║   МЕТОД ЦИКЛИЧЕСКОГО СДВИГА (С КЛЮЧЕВЫМ СЛОВОМ)   ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ                       ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ                      ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ * --- НАЗАД                                       ║")
    print("╚═══════════════════════════════════════════════════╝")
    print()
    R = ""
    N = input("ВАШ ВЫБОР: ")
    if N == "1":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            m = RESULT
        elif R == "2":
            m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._3_encrypt_method_kvadrat_polobia_kluch(m,k))
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "2":
        print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
        print("*** 1 --- ДА  ***")
        print("*** 2 --- НЕТ ***")
        R = input("ВАШ ОТВЕТ: ")
        if R == "1":
            c = RESULT
        elif R == "2":
            c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
        k = input("ВВЕДИТЕ КЛЮЧ (СЛОВО): ")
        print()
        print("ВАШ ТЕКСТ: ",C1._3_decrypt_method_kvadrat_polobia_kluch(c,k))
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif N == "*":
        print()
        print("OK!")
        _3_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA) 
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
    return ""

def _1_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) МЕТОД СДВИГА ПО СТОЛБЦАМ ( МЕТОД ПРОСТОЙ ЗАМЕНЫ )'''
    print()
    print("╔══════════════════════════════╗")
    print("║   МЕТОД СДВИГА ПО СТОЛБЦАМ   ║")
    print("╠══════════════════════════════╣")
    print("║ 1 --- БЕЗ КЛЮЧЕВОГО СЛОВА    ║")
    print("╠══════════════════════════════╣")
    print("║ 2 --- С КЛЮЧЕВЫМ СЛОВОМ      ║")
    print("╠══════════════════════════════╣")
    print("║ * --- НАЗАД                  ║")
    print("╚══════════════════════════════╝")
    print()
    global MENU_POLIBIA_N
    MENU_POLIBIA_N = input("ВАШ ВЫБОР: ")
    if MENU_POLIBIA_N == "1":
        _1_method_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "2":
        _1_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "*":
        print()
        print("OK!")
        C(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _1_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
    return ""

def _2_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК ( МЕТОД ПРОСТОЙ ЗАМЕНЫ )'''
    print()
    print("╔═══════════════════════════════╗")
    print("║ МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК ║")
    print("╠═══════════════════════════════╣")
    print("║ 1 --- БЕЗ КЛЮЧЕВОГО СЛОВА     ║")
    print("╠═══════════════════════════════╣")
    print("║ 2 --- С КЛЮЧЕВЫМ СЛОВОМ       ║")
    print("╠═══════════════════════════════╣")
    print("║ * --- НАЗАД                   ║")
    print("╚═══════════════════════════════╝")
    print()
    global MENU_POLIBIA_N
    MENU_POLIBIA_N = input("ВАШ ВЫБОР: ")
    if MENU_POLIBIA_N == "1":
        _2_method_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "2":
        _2_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "*":
        print()
        print("OK!")
        C(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _2_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
    return ""

def _3_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA):
    '''Функция МЕНЮ (ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ) МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК ( МЕТОД ПРОСТОЙ ЗАМЕНЫ )'''
    print()
    print("╔═══════════════════════════════╗")
    print("║   МЕТОД ЦИКЛИЧЕСКОГО СДВИГА   ║")
    print("╠═══════════════════════════════╣")
    print("║ 1 --- БЕЗ КЛЮЧЕВОГО СЛОВА     ║")
    print("╠═══════════════════════════════╣")
    print("║ 2 --- С КЛЮЧЕВЫМ СЛОВОМ       ║")
    print("╠═══════════════════════════════╣")
    print("║ * --- НАЗАД                   ║")
    print("╚═══════════════════════════════╝")
    print()
    global MENU_POLIBIA_N
    MENU_POLIBIA_N = input("ВАШ ВЫБОР: ")
    if MENU_POLIBIA_N == "1":
        _3_method_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "2":
        _3_method_s_kluchom_polibia(MENU_POLIBIA_N)
    elif MENU_POLIBIA_N == "*":
        print()
        print("OK!")
        C(MENU)
    else:
        print("Вы ввели неверное значение попробуйте снова...")
        print()
        input("Нажмите Enter для продолжения...")
        _3_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
    return ""

def C(MENU):
    '''МЕНЮ ВЫПОЛНЕНИЯ ПЕРЕСТАНОВОЧНЫХ ШИФРОВ'''
    if MENU == "1":
        print()
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                   ШИФР «КВАДРАТ ПОЛИБИЯ»                          ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 1 --- МЕТОД СДВИГА ПО СТОЛБЦАМ (С КЛЮЧЕВЫМ СЛОВОМ)                ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 2 --- МЕТОД ЗАМЕНЫ СТОЛБЦОВ И СТРОК (С КЛЮЧЕВЫМ СЛОВОМ)           ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ 3 --- МЕТОД ЦИКЛИЧЕСКОГО СДВИГА (С КЛЮЧЕВЫМ СЛОВОМ)               ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")  
        print()
        global MENU_POLIBIA
        MENU_POLIBIA = input("ВАШ ВЫБОР: ")
        if MENU_POLIBIA == "1":
            _1_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
        elif MENU_POLIBIA == "2":
            _2_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
        elif MENU_POLIBIA == "3":
            _3_METHOD_KVADRAT_POLIBIA(MENU_POLIBIA)
        elif MENU_POLIBIA == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_C(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            C(MENU)
        return ""
            
    elif MENU == "2":
        print()
        print("╔══════════════════════════════╗")
        print("║    ШИФР ЧЕТЫРЁХ КВАДРАТОВ    ║")
        print("║══════════════════════════════║")
        print("║ 1 --- ЗАШИФРОВАТЬ СООБЩЕНИЕ  ║")
        print("╠══════════════════════════════╣")
        print("║ 2 --- РАСШИФРОВАТЬ СООБЩЕНИЕ ║")
        print("╠══════════════════════════════╣")
        print("║ * --- НАЗАД                  ║")
        print("╚══════════════════════════════╝")
        print()
        R = ""
        N = input("ВАШ ВЫБОР: ")
        if N == "1":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                m = RESULT
            elif R == "2":
                m = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                C(MENU)
            k1 = input("ВВЕДИТЕ ВАШ ПЕРВЫЙ КЛЮЧ (СЛОВО): ")
            k2 = input("ВВЕДИТЕ ВАШ ВТОРОЙ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",C1._encrypt_4_kvadrata(m,k1,k2))
            print()
            input("Нажмите Enter для продолжения...")
            C(MENU)
        elif N == "2":
            print("ХОТИТЕ ЛИ ВЫ ИСПОЛЬЗОВАТЬ ПРОШЛОЕ ЗНАЧЕНИЕ?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            R = input("ВАШ ОТВЕТ: ")
            if R == "1":
                c = RESULT
            elif R == "2":
                c = input("ВВЕДИТЕ ВАШЕ ОТКРЫТОЕ СООБЩЕНИЕ: ")
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                C(MENU)
            k1 = input("ВВЕДИТЕ ВАШ ПЕРВЫЙ КЛЮЧ (СЛОВО): ")
            k2 = input("ВВЕДИТЕ ВАШ ВТОРОЙ КЛЮЧ (СЛОВО): ")
            print()
            print("ВАШ ТЕКСТ: ",C1._decrypt_4_kvadrata(c,k1,k2))
            print()
            input("Нажмите Enter для продолжения...")
            C(MENU)
        elif N == "*":
            print()
            print("OK!")
            main_menu_my_program.MENU_C(main_menu)
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            C(MENU)
        return ""

class main_menu_my_program:
    
    def MENU_A(main_menu):
        '''МЕНЮ ПОДСТАНОВОНЫХ ШИФРОВ'''
        print()
        print("╔═══════════════════════════════════════════╗")
        print("║           ПОДСТАНОВОЧНЫЕ ШИФРЫ            ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 1 --- ШИФР ЦЕЗАРЯ                         ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 2 --- ШИФР АТБАШ                          ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 3 --- ШИФР ЗАМЕНЫ                         ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 4 --- ШИФР ЗАМЕНЫ С КОДОВЫМ СЛОВОМ        ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 5 --- ШИФР БЭКОНА                         ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 6 --- ШИФР ВИЖЕНЕРА                       ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 7 --- ШИФР ВЕРНАМА (ОДНОРАЗОВЫЕ БЛОКНОТЫ) ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ * --- НАЗАД                               ║")
        print("╚═══════════════════════════════════════════╝")    
        print()
        global MENU
        MENU = input("ВАШ ВЫБОР: ")
        if MENU == "1" or MENU == "2" or MENU == "3" or MENU == "4" or MENU == "5" or MENU == "6" or MENU == "7":
            A(MENU)
        elif MENU == "*":
            print()
            print("OK!")
            main_menu_my_program.main_global_menu()
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            main_menu_my_program.MENU_A(main_menu)
        return MENU

    def MENU_B(main_menu):
        '''МЕНЮ ПЕРЕСТАНОВОЧНЫЕ ШИФРЫ'''
        print()
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                     ПЕРЕСТАНОВОЧНЫЕ ШИФРЫ                      ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 1 --- ШИФР «СКИТАЛА»                                           ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 2 --- ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР                  ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 3 --- ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР С КЛЮЧОМ         ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 4 --- ПРОСТОЙ СТОЛБЦОВЫЙ ПЕРЕСТАНОВОЧНЫЙ ШИФР С КОДОВЫМ СЛОВОМ ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                                    ║")
        print("╚════════════════════════════════════════════════════════════════╝")    
        print()
        global MENU
        MENU = input("ВАШ ВЫБОР: ")
        if MENU == "1" or MENU == "2" or MENU == "3" or MENU == "4":
            B(MENU)
        elif MENU == "*":
            print()
            print("OK!")
            main_menu_my_program.main_global_menu()
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            main_menu_my_program.MENU_B(main_menu)
        return MENU
    
    def MENU_C(main_menu):
        '''МЕНЮ ШИФРОВ, СВЯЗАННЫХ С ВНЕСЕНИЕМ АЛФАВИТА В КВАДРАТНУЮ МАТРИЦУ'''
        print()
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║   ШИФРЫ, СВЯЗАННЫЕ С ВНЕСЕНИЕМ АЛФАВИТА В КВАДРАТНУЮ МАТРИЦУ   ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 1 --- ШИФР «КВАДРАТ ПОЛИБИЯ»                                   ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ 2 --- ШИФР ЧЕТЫРЁХ КВАДРАТОВ                                   ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║ * --- НАЗАД                                                    ║")
        print("╚════════════════════════════════════════════════════════════════╝")    
        print()
        global MENU
        MENU = input("ВАШ ВЫБОР: ")
        if MENU == "1" or MENU == "2":
            C(MENU)
        elif MENU == "*":
            print()
            print("OK!")
            main_menu_my_program.main_global_menu()
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            main_menu_my_program.MENU_C(main_menu)
        return MENU
            
    def main_global_menu():
        print()
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║                        Главное МЕНЮ                              ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║ A --- Подстановочные шифры                                       ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║ B --- Перестановочные шифры                                      ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║ C --- Шифры, связанные с внесением алфавита в квадратную матрицу ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║ * --- ВЫХОД                                                      ║")
        print("╚══════════════════════════════════════════════════════════════════╝")
        print()
        L = ""
        global main_menu
        main_menu = input("ВАШ ВЫБОР: ")
        if main_menu == "A" or main_menu == "a" or main_menu == "А" or main_menu == "а" or main_menu == "1":
            main_menu_my_program.MENU_A(main_menu)
        elif main_menu == "B" or main_menu == "b" or main_menu == "В" or main_menu == "в" or main_menu == "Б" or main_menu == "б" or main_menu == "2":
            main_menu_my_program.MENU_B(main_menu)
        elif main_menu == "C" or main_menu == "c" or main_menu == "С" or main_menu == "с" or main_menu == "3":
            main_menu_my_program.MENU_C(main_menu) 
        elif MENU == "*":
            print()
            print("OK!")
            print("Вы точно хотите завершить работу программы?")
            print("*** 1 --- ДА  ***")
            print("*** 2 --- НЕТ ***")
            L = input("ВАШ ОТВЕТ: ")
            if L == "1":
                sys.exit(0)
            elif L == "2":
                main_menu_my_program().main_global_menu()
            else:
                print("Вы ввели неверное значение попробуйте снова...")
                print()
                input("Нажмите Enter для продолжения...")
                main_menu_my_program().main_global_menu()
        else:
            print("Вы ввели неверное значение попробуйте снова...")
            print()
            input("Нажмите Enter для продолжения...")
            main_menu_my_program().main_global_menu()
print()            
print("╔════════════════════════════════════════════════════════════════════╗")
print("║                        ***ДОБРО ПОЖАЛОВАТЬ!***                     ║")
print("╠════════════════════════════════════════════════════════════════════╣")
print("║ Эта программа предназначена для шифрования/дешифрования сообщений! ║")
print("║ Нажмите Enter, чтобы запустить Главное МЕНЮ =)                     ║")
print("╚════════════════════════════════════════════════════════════════════╝")
input("                             *** ТЫК ***                              ")
main_menu_my_program.main_global_menu()
