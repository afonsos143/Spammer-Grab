import pyautogui, time
time.sleep(5)
okuma = open("test", 'r')
for word in okuma:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
        return False, 'exception', True
    if req.status_code == 429:
        return False, 'reached limit', True
    elif req.status_code == 200:
        return True, '200 ok', True
    else:
        raise NotImplementedError(
            'something went wrong, please submit an issue.')


if __name__ == '__main__':
    click.secho(f'{sys.argv[0]} \u2014 Grab Activation Code (GAC) spammer',
                fg='black',
                bg='green')
    click.echo(' author\tloncat <me@lcat.dev>')
    click.echo(' url\thttps://github.com/p4kl0nc4t/Spammer-Grab\n')
    main()
