from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        # إنشاء التصميم الأساسي
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # إضافة عنوان الترحيب
        self.label = Label(
            text='Welcome to Hello World App!',
            font_size='24sp',
            color=(0.2, 0.6, 0.8, 1),  # لون النص
            halign='center',
        )
        layout.add_widget(self.label)
        
        # إضافة زر "Start"
        start_button = Button(
            text='Start',
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.1, 0.5, 0.3, 1),  # لون الزر
            font_size='20sp'
        )
        start_button.bind(on_press=self.on_start_press)
        layout.add_widget(start_button)
        
        return layout
    
    def on_start_press(self, instance):
        # تحديث النص عند الضغط على الزر
        self.label.text = 'You pressed Start! Enjoy the App!'

# تشغيل التطبيق
if __name__ == '__main__':
    HelloWorldApp().run()