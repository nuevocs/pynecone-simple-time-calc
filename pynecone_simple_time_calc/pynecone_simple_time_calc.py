from pcconfig import config

import pynecone as pc
from datetime import datetime, date, timedelta

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    start_time: str = ""
    end_time: str = ""
    mid_end: str = ""
    mid_start: str = ""
    mid_end_2: str = ""
    mid_start_2: str = ""
    result: str = ""
    show: bool = False
    working_hour: int = 7
    working_minute: int = 30

    def time_calc(self):
        def calc(start_time, end_time):
            start_time = datetime.strptime(start_time, "%H:%M").time()
            end_time = datetime.strptime(end_time, "%H:%M").time()
            result = str(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
            return result

        def mid_duration_calc(mid_end, mid_start):
            try:
                mid_end = datetime.strptime(mid_end, "%H:%M").time()
                mid_start = datetime.strptime(mid_start, "%H:%M").time()
                mid_delta_diff = datetime.combine(date.today(), mid_start) - datetime.combine(date.today(), mid_end)

                return mid_delta_diff
            except ValueError:
                return None

        expected_working_duration = timedelta(hours=(int(self.working_hour) + 1), minutes=int(self.working_minute))
        expected_endtime = datetime.combine(date.today(), datetime.strptime(self.start_time,
                                                                            "%H:%M").time()) + expected_working_duration
        multiple_not_working = [mid_duration_calc(self.mid_end, self.mid_start),
                                mid_duration_calc(self.mid_end_2, self.mid_start_2)]

        if multiple_not_working[0] is not None and multiple_not_working[1] is None and self.mid_end != "":

            final_working_endtime = expected_endtime + multiple_not_working[0]
            final_working_endtime.strftime("%H:%M")
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")
        elif not None in multiple_not_working and self.mid_end != "":
            multiple_not_working = sum(multiple_not_working, timedelta())
            final_working_endtime = expected_endtime + multiple_not_working
            final_working_endtime.strftime("%H:%M")
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")

        else:
            final_working_endtime = expected_endtime
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")

    def reset_inputs(self):
        # self.start_time = ""
        self.end_time = ""
        self.mid_end = ""
        self.mid_start = ""
        self.mid_end_2 = ""
        self.mid_start_2 = ""
        self.result = ""

    def change(self):
        self.show = not (self.show)


def pc_text_for_input(text, color, size, **kwargs):
    return pc.text(text, color_scheme=color, font_size=size, **kwargs)


def pc_span_for_input(text, color, size, weight):
    return pc.span(text, color_scheme=color, font_size=size, font_weight=weight)


def index() -> pc.Component:
    return pc.container(
        pc.vstack(
            pc.heading("Until what time will I work today? 🤔", font_size="1.4em"),
            pc.hstack(
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Start time: ", "black", "0.5em", "normal"),
                        pc_span_for_input(State.start_time, "blue", "1em", "bold"),
                    ),

                    pc.hstack(
                        pc.box(
                            pc.input(on_change=State.set_start_time, placeholder="10:00", bg="white"),
                            width="50%",
                        ),
                        pc.box(
                            pc.number_input(on_change=State.set_working_hour, default_value=7, bg="white"),
                            width="20%",
                        ),
                        pc.box(
                            pc.number_input(on_change=State.set_working_minute, default_value=30, bg="white"),
                            width="20%",
                        ),
                        pc.box(
                            pc.text("+1h lunch break", font_size="0.2em"),
                            width="10%",
                        ),

                    ),

                ),
            ),
            pc.hstack(
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Going out time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_end, "blue", "1em", "bold"),
                    ),
                    pc.input(on_change=State.set_mid_end, placeholder="15:00", bg="white"),
                ),
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Re-entry time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_start, "blue", "1em", "bold"),
                    ),
                    pc.input(on_change=State.set_mid_start, placeholder="16:13", bg="white"),
                ),
            ),

            # 2nd mid-items
            pc.hstack(
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Going out time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_end_2, "blue", "1em", "bold"),
                    ),
                    pc.input(on_change=State.set_mid_end_2, placeholder="15:00", bg="white"),
                ),
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Re-entry time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_start_2, "blue", "1em", "bold"),
                    ),
                    pc.input(on_change=State.set_mid_start_2, placeholder="16:13", bg="white"),
                ),
            ),

            pc.spacer(),

            pc.hstack(
                pc.button(
                    "Result", color="white", bg="green",
                    on_click=[State.change, State.time_calc],
                ),
                pc.alert_dialog(
                    pc.alert_dialog_overlay(
                        pc.alert_dialog_content(
                            pc.alert_dialog_header("Here you go!"),
                            pc.alert_dialog_body(
                                State.result
                            ),
                            pc.alert_dialog_footer(
                                pc.button(
                                    "Close",
                                    on_click=State.change,
                                )
                            ),
                        )
                    ),
                    is_open=State.show,
                ),
                pc.button(
                    "Reset",
                    on_click=State.reset_inputs
                ),
            ),

            bg="#e3e3e3",
            margin="5em",
            padding="1em",
            border_radius="0.5em",
            shadow="lg",
        ),
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
