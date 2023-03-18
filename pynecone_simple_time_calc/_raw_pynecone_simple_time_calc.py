"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
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
    mid_items: list = []

    def reset_inputs(self):
        self.start_time = ""
        self.end_time = ""
        self.mid_end = ""
        self.mid_start = ""
        self.mid_end_2 = ""
        self.mid_start_2 = ""
        self.result = ""

    def mid_itmes_append(self):
        # self.mid_items = []
        self.mid_items.append(self.mid_items)

    def textconcat(self):
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

        expected_working_duration = timedelta(hours=8, minutes=30)
        expected_endtime = datetime.combine(date.today(), datetime.strptime(self.start_time,
                                                                            "%H:%M").time()) + expected_working_duration
        multiple_not_working = [mid_duration_calc(self.mid_end, self.mid_start), mid_duration_calc(self.mid_end_2, self.mid_start_2)]
        # multiple_not_working = sum(multiple_not_working, timedelta())

        if multiple_not_working[0] is not None and multiple_not_working[1] is None:

            final_working_endtime = expected_endtime + multiple_not_working[0]
            final_working_endtime.strftime("%H:%M")
            # print(final_working_endtime.strftime("%H:%M"))
            # self.result = "You must work by " + str(final_working_endtime.time())
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")
        elif not None in multiple_not_working:
            multiple_not_working = sum(multiple_not_working, timedelta())
            final_working_endtime = expected_endtime + multiple_not_working
            final_working_endtime.strftime("%H:%M")
            # print(final_working_endtime.strftime("%H:%M"))
            # self.result = "You must work by " + str(final_working_endtime.time())
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")

        else:
            final_working_endtime = expected_endtime
            self.result = "You are expected to go on duty at " + final_working_endtime.strftime("%H:%M")

    def change(self):
        self.show = not (self.show)


def pc_text_for_input(text, color, size, **kwargs):
    return pc.text(text, color_scheme=color, font_size=size, **kwargs)


def pc_span_for_input(text, color, size, weight):
    return pc.span(text, color_scheme=color, font_size=size, font_weight=weight)

class MidState(State):
    end_time_2: str = ""
    start_time_2: str = ""


class ObjState(State):
    items: list = []
    items2: list = []
    new_item: str = ""
    new_item2: str = ""

    def add_item(self):
        self.items += [[self.new_item, "-", self.new_item2]]
        self.items2 += [self.new_item2]
        self.new_item = ""
        self.new_item2 = ""

    def finish_item(self, item):
        self.items = [i for i in self.items if i != item]


def render_item(item):
    """Render an item in the todo list."""
    return pc.list_item(
        pc.hstack(
            pc.button(
                on_click=lambda: ObjState.finish_item(item),
                height="1.5em",
                background_color="white",
                border="1px solid blue",
            ),
            pc.text(item, font_size="1.25em"),
        )
    )
def repeat_item(item):
    return pc.text(item, font_size="1.25em")

def index() -> pc.Component:
    return pc.container(
        pc.vstack(
            pc.heading("Until what time will I work today? 🤔", font_size="1.4em"),
            # pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.hstack(
                pc.vstack(
                    pc.box(
                        # pc_text_for_input("Start time: "+State.start_time, "green", "0.4em"),
                        # pc.span("Start time:  ", color="black", font_size="0.3em"),
                        pc_span_for_input("Start time: ", "black", "0.5em", "normal"),
                        pc_span_for_input(State.start_time, "blue", "1em", "bold"),
                    ),
                    # pc.text("Start time: "+State.start_time, color_scheme="green"),
                    pc.input(on_change=State.set_start_time, placeholder="10:00", bg="white"),
                ),
                # pc.vstack(
                #     pc.text(State.end_time, color_scheme="red"),
                #     pc.input(on_change=State.set_end_time),
                # ),
            ),
            pc.hstack(
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Going out time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_end, "blue", "1em", "bold"),
                        # pc.text("Going out time: " + State.mid_end, color_scheme="red"),
                    ),
                    pc.input(on_change=State.set_mid_end, placeholder="15:00", bg="white"),
                ),
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Re-entry time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_start, "blue", "1em", "bold"),
                        # pc.text("Re-entry time: " + State.mid_start, color_scheme="red"),
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
                        # pc.text("Going out time: " + State.mid_end, color_scheme="red"),
                    ),
                    pc.input(on_change=State.set_mid_end_2, placeholder="15:00", bg="white"),
                ),
                pc.vstack(
                    pc.box(
                        pc_span_for_input("Re-entry time:", "black", "0.5em", "normal"),
                        pc_span_for_input(State.mid_start_2, "blue", "1em", "bold"),
                        # pc.text("Re-entry time: " + State.mid_start, color_scheme="red"),
                    ),
                    pc.input(on_change=State.set_mid_start_2, placeholder="16:13", bg="white"),
                ),
            ),
            # pc.button(
            #     "Calculate", bg="orange", color="white", size="md", on_click=State.textconcat,
            # ),
            pc.hstack(
                pc.button(
                    "Result",
                    on_click=[State.change, State.textconcat],
                ),
                pc.alert_dialog(
                    pc.alert_dialog_overlay(
                        pc.alert_dialog_content(
                            pc.alert_dialog_header("Here you go!"),
                            pc.alert_dialog_body(
                                State.result
                                # "Do you want to confirm example?"
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

            pc.divider(),

            pc.hstack(
                pc.input(
                    on_blur=ObjState.set_new_item,
                    placeholder="Add a todo...",
                    bg="white",
                ),
                pc.input(
                    on_blur=ObjState.set_new_item2,
                    placeholder="Add 2 a todo...",
                    bg="white",
                ),
            ),
            pc.button("Add", on_click=ObjState.add_item, bg="white"),

            pc.ordered_list(
                pc.foreach(ObjState.items, lambda item: render_item(item)),
            ),
            # pc.ordered_list(
            #     pc.foreach(ObjState.items, lambda item: repeat_item(item)),
            # ),

            # pc.text(ObjState.items[0], ),




            # pc.ordered_list(
            #     pc.text(ObjState.items, lambda item: render_item(item)),
            # ),

            # pc.text(State.result, font_size="2em"),
            # pc.link(
            #     "Check out our docs!",
            #     href=docs_url,
            #     border="0.1em solid",
            #     padding="0.5em",
            #     border_radius="0.5em",
            #     _hover={
            #         "color": "rgb(107,99,246)",
            #     },
            # ),
            # spacing="1.5em",
            # font_size="2em",
            # padding_top="10%",
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
