from kivy.app import App
from kivy.core.window import Window
from jnius import autoclass, cast

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
KeyEvent = autoclass('android.view.KeyEvent')

class CallControlApp(App):
    def build(self):
        Window.bind(on_key_down=self.on_key_down)
        return

    def on_key_down(self, window, keycode, scancode, codepoint, modifiers):
        activity = PythonActivity.mActivity
        context = cast('android.content.Context', activity.getApplicationContext())
        telecom = cast('android.telecom.TelecomManager', context.getSystemService(Context.TELECOM_SERVICE))

        if keycode == KeyEvent.KEYCODE_VOLUME_UP:
            print("🔔 VOL+ detectado")
            try:
                if telecom and telecom.isRinging():
                    telecom.acceptRingingCall()
                    print("✅ Llamada aceptada")
            except Exception as e:
                print(f"❌ Error al aceptar llamada: {e}")

        elif keycode == KeyEvent.KEYCODE_VOLUME_DOWN:
            print("🔕 VOL- detectado — colgar requiere permisos especiales en Android 5")

        return True

if __name__ == '__main__':
    CallControlApp().run()
