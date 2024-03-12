types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def delete_duplicate_tickets(input_dict):
    new_tickets = {}
    duplicate_tickets = set()
    for key in input_dict.keys():
        new_tickets[key] = []
        for ticket in input_dict[key]:
            if ticket not in duplicate_tickets:
                new_tickets[key].append(ticket)
                duplicate_tickets.add(ticket)
    return new_tickets


def link_tickets_types(input_key, inmput_value):
    new_tickets = delete_duplicate_tickets(inmput_value)
    tickets_by_type = {}
    for key, value in input_key.items():
        if key in new_tickets:
            tickets_by_type[value] = new_tickets[key]
    return tickets_by_type


print(link_tickets_types(types, tickets))
