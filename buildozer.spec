[app]

# اسم التطبيق
title = HelloWorldApp
package.name = helloworldapp
package.domain = org.helloworldapp

# تحديد الإصدار
version = 1.0.0

# الدليل الذي يحتوي على الكود
source.dir = .

# الحزم المطلوبة
dependencies = python3, kivy

# الأذونات المطلوبة
android.permissions = INTERNET

[buildozer]

# استخدام pip لتثبيت الحزم
use_pip = True