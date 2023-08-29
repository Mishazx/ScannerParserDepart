import PyPDF2
import g4f
from PyQt5.QtCore import Qt, QThread, pyqtSignal


document_types = {
    "Юридический": ["договор", "судебное разбирательство", "правовой", "адвокат", "претензия", "консультация юриста", "правовая практика",
                    "исковое заявление", "юридическая консультация", "лицензирование", "подпись документов", "правообладатель", "судебный процесс",
                    "уголовное дело", "законодательство", "нотариус", "правовая система", "гражданское право", "административное право", "трудовое право",
                    "корпоративное право", "международное право", "коммерческое право", "семейное право", "налоговое право", "конституционное право",
                    "криминальное право", "правовая норма", "судебное решение", "правовая ответственность", "юридическая деятельность", "юридическая экспертиза",
                    "арбитражное право", "гражданский кодекс", "адвокатская практика", "правовой акт", "правовая защита", "юридическое образование",
                    "юридическая литература", "юридический анализ", "правовая наука", "лицензирование деятельности", "адвокатские услуги", "законодательные акты",
                    "правовой статус", "судебная практика", "юридическая помощь", "юридический факультет", "правовая реформа", "юридическое лицо",
                    "юридическое лицо", "правовая поддержка", "правовой консультант", "практика применения права", "юридическое консультирование",
                    "юридическая процедура", "правовое регулирование", "сделка", "арбитражный суд", "конституционный суд", "исполнительное производство",
                    "юридический словарь", "переговоры", "адвокатский кабинет", "судебная практика", "гражданский процесс", "административный процесс",
                    "юридическая ответственность", "юридическая практика", "правовая система", "судебное рассмотрение", "юридическая реформа",
                    "правовой стандарт", "правовое поле", "правовое сообщество", "арбитражный процесс", "процессуальное право", "публичное право",
                    "негосударственная организация", "юридическая профессия", "юридическая книга", "юридическое исследование", "судебная практика",
                    "юридический совет", "защита прав потребителей", "правовое решение", "правовой анализ", "правовой процесс", "арбитражное разбирательство",
                    "нарушение прав", "правовой советник", "юридическая экспертиза", "правовая гарантия", "юридический центр", "консультация по налоговому праву",
                    "правовая помощь бизнесу", "семинар по юридическим вопросам", "юридическая безопасность", "юридический университет", "юридическая психология",
                    "защита прав человека", "юридическая реабилитация"],

    "Бухгалтерия": ["финансы", "баланс", "отчетность", "налоги", "аудит", "финансовый отчет", "план счетов", "бухгалтерский учет", "консолидированный баланс",
                    "налоговая декларация", "финансовый анализ", "бухгалтерская отчетность", "расходы", "доходы", "бюджетирование", "налоговые ставки",
                    "бухгалтерские проводки", "комплексный анализ", "финансовое планирование", "бухгалтерский журнал", "амортизация", "учет активов",
                    "учет обязательств", "бухгалтерский баланс", "финансовый менеджмент", "бухгалтерская система", "кассовый отчет", "финансовые ресурсы",
                    "бухгалтерская программа", "финансовые инвестиции", "бухгалтерский аудит", "нормативно-правовая база", "налоговые выплаты",
                    "бухгалтерские нормы", "бухгалтерский бюджет", "контроллинг", "статьи доходов и расходов", "финансовые операции", "кредиторская задолженность",
                    "дебиторская задолженность", "финансовые отчеты", "финансовое регулирование", "анализ бухгалтерской отчетности", "валютные операции",
                    "финансовая устойчивость", "подоходный налог", "единый налог", "финансовая стратегия", "бухгалтерский кодекс", "финансовые показатели",
                    "ревизия", "финансовая консолидация", "учетная политика", "бухгалтерская книга", "затраты", "финансовая отчетность", "бухгалтерский отчет",
                    "налоговый учет", "бухгалтерские накопления", "декларирование доходов", "расчеты с поставщиками", "расчеты с клиентами", "счета на оплату",
                    "финансовые операции", "финансовое право", "ресурсосбережение", "страхование", "финансовый риск", "денежные средства", "перерасчеты",
                    "бухгалтерская отчетность", "финансовые инструменты", "операционные расходы", "пассивы", "активы", "финансовый контроль", "финансовый рынок",
                    "доход от продаж", "капитализация", "неденежные средства", "долгосрочные обязательства", "краткосрочные обязательства", "капитал",
                    "инвентаризация", "себестоимость", "доходы от инвестиций", "экономический анализ", "финансовое здоровье", "финансовый ресурс",
                    "инвестиционная деятельность", "финансовые прогнозы", "финансовый контроль", "дивиденды", "аудиторская проверка", "бюджетное планирование",
                    "финансовая структура", "амортизационные отчисления", "потоки денежных средств", "бюджетное управление", "финансовое регулирование",
                    "расчеты с сотрудниками", "бухгалтерский документооборот", "налоговый агент", "финансовый консультант", "финансовый инжиниринг",
                    "компенсационные выплаты", "финансовая децентрализация", "нормативные акты по бухгалтерии", "бухгалтерская отчетность", "финансовое управление",
                    "финансовый аудит", "налоговое планирование", "финансовая ответственность", "бухгалтерский архив", "финансовое обеспечение"],

    "Учебный": ["план учебы", "преподаватель", "студент", "лекция", "экзамен", "курсовая работа", "академическая программа", "учебные материалы", 
                "зачет", "диплом", "сессия", "выпускной экзамен", "учебный год", "оценки", "научные исследования", "научный руководитель", 
                "стипендия", "программа обучения", "аудитория", "группа", "семестр", "самостоятельная работа", "расписание занятий", "бакалавриат", 
                "магистратура", "аспирантура", "докторантура", "академическая дисциплина", "кредиты", "каникулы", "реферат", "проектная работа", 
                "практика", "научная конференция", "библиотека", "институт", "факультет", "кафедра", "стипендиат", "профессор", "ассистент", 
                "магистерская диссертация", "аспирант", "диссертация", "публикация", "студенческое самоуправление", "компьютерный класс",
                "студенческий билет", "проходные баллы", "академическая честность", "обмен студентов", "международные программы", 
                "вступительные испытания", "ректор", "декан", "завуч", "педагогический процесс", "аудиторская работа", "дистанционное обучение",
                "пересдача", "профессиональное образование", "научный журнал", "симпозиум", "тема исследования", "дистанционное образование",
                "педагогический опыт", "студенческая конференция", "подготовка к экзаменам", "подготовка к защите", "преподавательский состав",
                "поступление", "рейтинг студентов", "студенческий совет", "академическая карьера", "университет", "институт", "факультет", 
                "кампус", "лаборатория", "студенческая жизнь", "профориентация", "соревнования знаний", "консультации", "асессор", 
                "научное сообщество", "кафедра", "лектор", "студенческий проект", "учебный план", "контрольная работа", "методические указания",
                "магистерская программа", "докторская программа", "социальное обучение", "переводчик", "студенческий дом", "фельдшер", 
                "здравпункт", "студенческий клуб", "научный журнал", "профессиональные навыки", "образовательный процесс"],

    "Деканат": ["зачисление", "служебная записка", "академическая справка", "стипендия", "расписание занятий", "ректор", "декан", "ректорат", "советник при ректорате",
                "приказ о зачислении", "приказ об отчислении", "справка об обучении", "академический отпуск", "дипломная работа", "протокол заседания",
                "академическая дисциплина", "похвальная грамота", "заседание комиссии", "деканский совет", "выпускной бал", "учебный план", "подпись декана",
                "учебное расписание", "приемная комиссия", "академическая награда", "академическая этика", "деканский офис", "деканская должность", "распоряжение",
                "учебные группы", "распределение нагрузки", "контроль успеваемости", "деканская премия", "научный руководитель", "педагогический состав",
                "деканская конференция", "учебный процесс", "постановление деканата", "деканский список", "план обучения", "организация учебной работы",
                "распределение аудиторий", "проведение экзаменов", "деканская коллегия", "академическое руководство", "контроль аттестации", "учебно-методическая работа",
                "подготовка учебных материалов", "комплектование учебниками", "учебно-методический центр", "реализация учебного плана", "консультации студентов",
                "план научно-исследовательской работы", "контроль дисциплинарной ответственности", "академическая мобильность", "научно-педагогический совет",
                "учебно-научный процесс", "контроль посещаемости", "студенческий деканат", "методическая работа", "программа дисциплины", "поддержка студентов",
                "деканатский аппарат", "подготовка к защите диплома", "контроль учебных достижений", "разработка учебных планов", "согласование учебных программ",
                "ресурсное обеспечение", "индивидуальные графики обучения", "взаимодействие с преподавателями", "координация учебного процесса", "заведующий кафедрой", 
                "организация учебно-методической работы", "подготовка к выпускным мероприятиям", "деканский прием", "программа преддипломной практики",
                "академический статус", "мониторинг учебного процесса", "академический календарь", "деканатские обязанности", "профориентационная работа",
                "академическая поддержка", "комплектация учебных кабинетов", "проведение академических мероприятий", "учебное пособие", "анализ успеваемости",
                "подготовка отчетности деканата", "организация студенческой жизни", "мониторинг качества образования", "выпускной альбом", "контрольные мероприятия",
                "консультации по выбору специальности", "оценка учебной деятельности", "подготовка к научным конференциям", "кадровое обеспечение деканата",
                "планирование учебного процесса", "поддержка студенческих инициатив", "разрешение учебных вопросов", "деканская нагрузка"],

    "Охрана":  ["безопасность", "пожарная безопасность", "инструкция по охране труда", "персональная защита", "аварийный выход", "санитарные нормы",
                "охранник", "план эвакуации", "обучение по охране труда", "пожарная тревога", "контроль доступа", "видеонаблюдение", "профилактика травм",
                "охранное оборудование", "охранная служба", "охранная система", "охранное предприятие", "охранно-пропускной режим", "система тревожной сигнализации",
                "охранная сигнализация", "соблюдение правил охраны", "охранное задание", "дежурство охраны", "охрана объекта", "охранная деятельность",
                "охранно-пожарная сигнализация", "камеры наблюдения", "контрольно-пропускной пункт", "охранная служба", "охрана государственных объектов",
                "охрана имущества", "охранно-патрульная служба", "охранная компания", "охранное устройство", "система безопасности", "охраняемая территория",
                "безопасность на производстве", "охрана рабочего места", "профилактика краж", "доступ к конфиденциальной информации", "охранное задание",
                "система контроля и управления доступом", "безопасность персонала", "пожарные устройства", "охрана частной собственности", "система охранного видеонаблюдения",
                "соблюдение стандартов безопасности", "охрана жизни и здоровья", "охрана транспорта", "профессиональное обучение охране", "комплексная безопасность",
                "охрана на мероприятиях", "охранная лицензия", "мониторинг безопасности", "контрольно-пропускной режим", "барьерная система", "охранное законодательство",
                "система контроля доступа", "дежурство на посту охраны", "обеспечение общественной безопасности", "охрана государственных секретов",
                "охранно-досмотровые мероприятия", "биометрическая идентификация", "система оповещения", "патрулирование территории", "охранное обеспечение",
                "профессиональные стандарты охраны", "охранно-розыскная деятельность", "охранная система безопасности", "обеспечение пожарной безопасности",
                "безопасность информации", "пожарные учения", "электронная пропускная система", "охранное сообщество", "контрольно-пропускной режим",
                "пожаротушение", "система тревожной сигнализации", "система оповещения при аварии", "обучение по охране окружающей среды", "охрана окружающей среды",
                "технические средства охраны", "охранно-консультационный центр", "охранно-режимные мероприятия", "кризисное управление в охране"]
}

def analyze_text_with_g4f(text):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.DeepAi,
        messages=[{"role": "user", "content": f"Проанализируй данный текст и напиши как можно больше ключевых слов:\n{text}"}]
        #stream=True,
    )
    
    return response


# the function analyzes the text through OpenAI
# def analyze_text_with_gpt3(text):
#     string = f"Проанализируй данный текст и напиши как можно больше ключевых слов:\n{text}"
#     response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=string,
#     max_tokens=1500 
#     )
#     print(response)

#     analysis = response.choices[0].text.strip()
#     return analysis

# the function exports text from pdf
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    non_empty_lines = [line for line in text.splitlines() if line.strip()]
    result = '\n'.join(non_empty_lines)
    return result[:2000]

# the function determines type of department to send the document to
def classify_document_type(keywords_from_openai):
    best_match = None
    best_match_score = 0
    threshold=0.2

    keywords_from_openai = ''.join([keyword.lower() for keyword in keywords_from_openai])
    keywords_from_openai = keywords_from_openai.split(", ")
    # print(keywords_from_openai) # Debug!

    for doc_type, keywords in document_types.items():
        match_score = len(set(keywords_from_openai) & set(keywords))
        similarity = match_score / len(keywords)

        if similarity > best_match_score:
            best_match = doc_type
            best_match_score = similarity

    if best_match_score < threshold:
        closest_match = None
        closest_similarity = 0
        
        for doc_type, keywords in document_types.items():
            match_score = len(set(keywords_from_openai) & set(keywords))
            similarity = match_score / len(keywords)
            
            if similarity > closest_similarity:
                closest_match = doc_type
                closest_similarity = similarity
        
        return closest_match if closest_similarity > threshold else best_match
    else:
        return best_match


# the function return type of department
def engine(path):
    pdf_text = extract_text_from_pdf(path)
    key = analyze_text_with_g4f(pdf_text)
    # print(type(key))
    # if type(key) == openai
    return classify_document_type(key)


class OperationThread(QThread):
    operation_complete = pyqtSignal(str)
    
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.result = None

        self.current_retry = 0
        self.max_retries = 2
        
    def run(self):
        self.result = self.engine(self.value)

        while self.current_retry < self.max_retries and self.result is None:
            result = self.engine(self.value)
            self.current_retry += 1
        
        if self.result is not None:
            self.operation_complete.emit(self.result)
        else:
            self.operation_complete.emit("Error: Maximum retries reached")


    def engine(self, path):
        pdf_text = extract_text_from_pdf(path)
        key = analyze_text_with_g4f(pdf_text)  
        return classify_document_type(key)
    
    def quit(self):
        self.terminate()

if __name__ == '__main__':
    print(engine('pdf/зав_отчисление.pdf'))