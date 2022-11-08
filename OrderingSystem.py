from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Button, Static, Footer, Header, Input
from textual.widget import Widget
from textual.containers import Container, Horizontal, Vertical

class Abdul_Gadgetz(App):

    CSS_PATH = "OrderingSystem.css"

    #bindings, key to press
    BINDINGS = [
        ('q', 'quit', 'Quit')
    ]

    #press Q to quit the program
    def action_quit(self) -> None:
        self.exit()
        pass

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Static(StoreName, id="title")
        yield Horizontal(
            Vertical(
                
                #container for phones
                Container(
                    PhoneWidget(),
                ),classes="container", id="container_phone"
                
            ),
            Vertical(

                 Container(
                    LaptopWidget(),
                 ),classes="container", id="container_laptop"
            ),
             Vertical(

                #container for tablet
                 Container(

                    TabletWidget(),

                ),classes="container", id="container_tablet"
            ),
             Vertical(

                #container for accessories
                Container(

                    AccessoriesWidget(),

                ),classes="container", id="container_accessories"
            ),
             Vertical(

                #container for checkout
                Container(

                    CheckOutDIsplay(),

                ),classes="container", id="container_checkout"
            ),
        )

        #add the functionalities

# Phone Widget
class PhoneWidget(Static):
    def compose(self) -> ComposeResult:
        #container for the phone products
        yield Container (
            #Product's Title
            Static(":mobile_phone:Android Phone", classes="header"),
            #buttons for phones
            Button("[b]TVC ABD BLACK[/b]\n 256GB \n PHP 12,000",id="android_phone1", classes="btn_phone"),
            Button("[b]ARC ABD BLACK[/b]\n 128GB\n PHP 15,000", id="android_phone2", classes="btn_phone"),
            Button("[b]BTS ABD PURPLE[/b]\n 512\n PHP 25,000", id="android_phone3", classes="btn_phone"),
        )

# Laptop Widget
class LaptopWidget(Static):
    def compose(self) -> ComposeResult:
        # Container for the Laptop products
        yield Container (
            #Product's title
            Static(":computer:Laptop", classes="header"),
            #buttons for laptop
            Button("[b]LPTP ABD Lenovo PhinkTad[/b]\n 1TB i9\n PHP 70,000", id="laptop1", classes="btn_laptop"),
            Button("[b]LPTP ABD MACDOOK PRO[/b]\n 512GB\n PHP 120,000", id="laptop2", classes="btn_laptop"),
            Button("[b]LPTP ABD ASOWS RUG[/b]\n 2TB RYZEN 5\n PHP 25,000", id="laptop3", classes="btn_laptop"),

        )

# Tablet Widget
class TabletWidget(Static):
    def compose(self) -> ComposeResult:
        #container for the Tablet products
        yield Container (
            #Product's Title
            Static(":mobile_phone:Tablet", classes="header"),
            #buttons for tablet
            Button("[b]TSP ABD jPAD[/b]\n 512GB\n PHP 80,000", id="tablet1", classes="btn_tablet"),
            Button("[b]DOP ABD TAB S8[/b]\n 128GB\n PHP 75,000", id="tablet2", classes="btn_tablet"),
            Button("[b]DAP1 ABD jPAD AIR[/b]\n 256GB\n PHP 45,000", id="tablet3", classes="btn_tablet"),
        )

# Accessories Widget
class AccessoriesWidget(Static):
    def compose(self) -> ComposeResult:
        #container for the Accessories Products
        yield Container (
            #Product's Title
            Static(":watch:Accessories", classes="header"),
            #buttons for accessories
            Button("[b]SMW ABD WATCH[/b]\n SMART WATCH\n PHP 5,000", id="acc1", classes="btn_acc"),
            Button("[b]ASP ABD PEN[/b]\n SMART PEN\n PHP 2,000", id="acc2", classes="btn_acc"),
            Button("[b]EBS ABD EARBUDS[/b]\n WIRELESS EARBUDS\n PHP 1,500", id="acc3", classes="btn_acc"),
        )

# Check out Display widget
class CheckOutDIsplay(Static):
    def compose(self) -> ComposeResult:
        yield Container (
            #put the output here
            Static(":clipboard:Checkout", classes="header"),
            Static("Products:", classes="header1"),
            Static("Subtotal:", classes="header1"),
            Static("Total:", classes="header1"),
            #input the payment of the user and subtract to the total
            Static("Customer Payment:", classes="header1"),
            Static("Change:", classes="header1"),
            Button("Proceed", classes="btn_size1" ),
        )

StoreName = "┏━━━┓┏━━┓╋┏━━━┓┏┓╋┏┓┏┓╋╋╋┏━━━┓┏━━━┓┏━━━┓┏━━━┓┏━━━┓┏━━━━┓┏━━━━┓\n┃┏━┓┃┃┏┓┃╋┗┓┏┓┃┃┃╋┃┃┃┃╋╋╋┃┏━┓┃┃┏━┓┃┗┓┏┓┃┃┏━┓┃┃┏━━┛┃┏┓┏┓┃┗━━┓━┃\n┃┃╋┃┃┃┗┛┗┓╋┃┃┃┃┃┃╋┃┃┃┃╋╋╋┃┃╋┗┛┃┃╋┃┃╋┃┃┃┃┃┃╋┗┛┃┗━━┓┗┛┃┃┗┛╋╋┏┛┏┛\n┃┗━┛┃┃┏━┓┃╋┃┃┃┃┃┃╋┃┃┃┃╋┏┓┃┃┏━┓┃┗━┛┃╋┃┃┃┃┃┃┏━┓┃┏━━┛╋╋┃┃╋╋╋┏┛┏┛\n┃┏━┓┃┃┗━┛┃┏┛┗┛┃┃┗━┛┃┃┗━┛┃┃┗┻━┃┃┏━┓┃┏┛┗┛┃┃┗┻━┃┃┗━━┓╋╋┃┃╋╋┏┛━┗━┓\n┗┛╋┗┛┗━━━┛┗━━━┛┗━━━┛┗━━━┛┗━━━┛┗┛╋┗┛┗━━━┛┗━━━┛┗━━━┛╋╋┗┛╋╋┗━━━━┛"


if __name__ == "__main__":
    app = Abdul_Gadgetz()
    app.run()