import curses

def render_color(stdscr, color_id: int):
    height, width = stdscr.getmaxyx()
    
    for y in range(height-1):
       stdscr.addstr(y, 0, ' ' * width, curses.color_pair(1))
    
    text = f'[{color_id + 1}]'
    
    y_pos = height // 2
    x_pos = (width - len(text)) // 2
    
    stdscr.addstr(y_pos, x_pos, text, curses.color_pair(2))
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    
    color_id = 255
    
    while True:
        stdscr.clear()
        render_color(stdscr, color_id)
        
        key = stdscr.getch()
        
        if key == curses.KEY_LEFT and color_id > 0:
            color_id -= 1
            curses.init_pair(1, -1, color_id)
            curses.init_pair(2, 255 - color_id, color_id)
            
        elif key == curses.KEY_RIGHT and color_id < 255:
            color_id += 1
            curses.init_pair(1, -1, color_id)
            curses.init_pair(2, 255 - color_id, color_id)
            
        elif key == ord('q'):
            break

curses.wrapper(main)
