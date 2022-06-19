def new_save(file: str, all: list) -> None:
    start_info = all[0]
    board = all[1]
    player = all[2]
    action_count = all[3]
    stage = all[4]
    message = all[5]
    
    with open(f'\\save\\{file}', 'w') as f:
        f.write(f'{start_info}\n{board}\n{player}\n{action_count}\n{stage}\n{message}')
