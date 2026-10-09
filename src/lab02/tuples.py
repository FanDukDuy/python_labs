def format_record(rec):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    if not isinstance(fio, str):
        raise TypeError
    if not isinstance(group, str):
        raise TypeError
    if not isinstance(gpa, (int, float)):
        raise TypeError
    fio = ' '.join(fio.split())
    group = group.strip()
    if fio == '':
        raise ValueError
    if group == '':
        raise ValueError
    if gpa < 0 or gpa > 5:
        raise ValueError
    words = fio.split()
    surname = words[0]
    if len(words) < 2:
        raise ValueError
    init = words[1][0].upper() + '.'
    if len(words) >= 3:
        init += words[2][0].upper() + '.'
    surname = surname[0].upper() + surname[1:].lower()
    return f'{surname} {init}, гр. {group}, GPA {gpa:.2f}'






    

     