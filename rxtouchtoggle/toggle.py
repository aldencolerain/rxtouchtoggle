import os
import signal
from subprocess import call
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from subprocess import call


# settings
APPINDICATOR_ID = 'touchtoggle'
ENABLED = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'touchpad-indicator-light-enabled.svg')
DISABLED = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'touchpad-indicator-light-disabled.svg')


# start touch toggle tray widget
def start():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, ENABLED, appindicator.IndicatorCategory.SYSTEM_SERVICES)

    def enable(source):
        indicator.set_icon(ENABLED)
        call("synclient TouchpadOff=0", shell=True)

    def disable(source):
        indicator.set_icon(DISABLED)
        call("synclient TouchpadOff=1", shell=True)

    # def quit(source):
    #     gtk.main_quit()

    def build_menu():
        menu = gtk.Menu()

        enable_item = gtk.MenuItem('Enable')
        enable_item.connect('activate', enable)
        menu.append(enable_item)

        disable_item = gtk.MenuItem('Disable')
        disable_item.connect('activate', disable)
        menu.append(disable_item)

        # quit_item = gtk.MenuItem('Close')
        # quit_item.connect('activate', quit)
        # menu.append(quit_item)

        # show menu
        menu.show_all()
        return menu

    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    #enable(None)
    gtk.main()
