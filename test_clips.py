
import clips


def main():
    env = clips.Environment()
    env.build('(defrule hello => (printout t "CLIPS works successfully" crlf))')
    env.reset()
    count = env.run()
    print(f"Спрацювало правил: {count}")


if __name__ == "__main__":
    main()
