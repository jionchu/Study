# TextView
### 일부 string에만 style 적용시키기
```java
TextView tvTitle;
String title = "Hello world"
SpannableString ss = new SpannableString(title);
StyleSpan boldSpan = new StyleSpan(Typeface.BOLD);
ss.setSpan(boldSpan, 0, 5, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
tvTitle.setText(ss);
```
- **Hello** world