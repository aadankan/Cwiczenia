[1mdiff --git a/drawings.py b/drawings.py[m
[1mindex b1ea99d..927d6c1 100644[m
[1m--- a/drawings.py[m
[1m+++ b/drawings.py[m
[36m@@ -30,19 +30,30 @@[m [mclass Drawing:[m
             i += 1 / r * d[m
             pyautogui.click(a+x, b-y, duration=wtime)[m
 [m
[31m-    def dom(self=2, x=100, y=100, h=50, wtime=0):[m
[32m+[m[32m    def elipse(self=2, w=100, h=50, d=1, wtime=0):[m
[32m+[m[32m        time.sleep(self)[m
[32m+[m[32m        i = 0[m
[32m+[m[32m        a, b = pyautogui.position()[m
[32m+[m[32m        while i <= 2 * pi:[m
[32m+[m[32m            x = round(sin(i) * w)[m
[32m+[m[32m            y = round(cos(i) * h)[m
[32m+[m[32m            i += 1 / w * d[m
[32m+[m[32m            pyautogui.click(a+x, b-y, duration=wtime)[m
[32m+[m
[32m+[m[32m    def dom(self=2, x=100, y=100, h=50, wtime=1.5):[m
         time.sleep(self)[m
         Drawing.prostokat(0, x, y, wtime)[m
         pyautogui.moveRel(-1 / 2 * x, 0)[m
         Drawing.trojkat(0, x, h, wtime)[m
         pyautogui.moveRel(3/5*x, 1/5*x)[m
[31m-        Drawing.prostokat(0, x/5, x/5)[m
[32m+[m[32m        Drawing.prostokat(0, x/5, x/5, wtime/2)[m
         pyautogui.moveRel(3/5*x, 0)[m
[31m-        Drawing.prostokat(0, x / 5, x / 5)[m
[32m+[m[32m        Drawing.prostokat(0, x / 5, x / 5, wtime/2)[m
         pyautogui.moveRel(-7/10*x, -1/5*x)[m
         pyautogui.moveRel(2/5*x,3/5*y)[m
[31m-        Drawing.prostokat(0, x/5, 12/30*y)[m
[32m+[m[32m        Drawing.prostokat(0, x/5, 12/30*y, wtime)[m
[32m+[m
 [m
 [m
[31m-Drawing.dom()[m
 [m
[32m+[m[32mDrawing.dom(x=100, y=100)[m
\ No newline at end of file[m
