from pynput import mouse

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(int(x), int(y))))
    if pressed:
        #dragp/x=700/y=500/dragduration=0.45/
        with open('rireki.txt', mode='a') as f:
            f.write(''+str(x)+'/'+str(y)+'\n')

# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()
