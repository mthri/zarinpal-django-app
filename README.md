# Zarinpal Django App

<h2 dir='rtl'>اپ پرداخت جنگو برای زرین‌پال</h2>
<p dir='rtl'>در این پروژه سعی شده یک مثال ساده برای پرداخت  با درگاه واسط بانکی زرین‌پال و ذخیره اطلاعات پرداخت در دیتابیس نوشته شود.</p>
<p dir='rtl'>این پروژه قابل بسط با توجه به نیاز شما میباشد بطور مثال می‌توانید فیلدی به نام <strong>user</strong> به مدل <strong>Transaction</strong> اضافه کنید و به مدل <a href='https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#user-model'>User</a> متصل کنید. </p>

<p dir='rtl'> برای استفاده از سیستم <a href='https://next.zarinpal.com/paymentGateway/sandbox.html'>Sandbox</a> کافی است از همین کد استفاده کنید.</p>

<p dir='rtl'><strong>توجه:</strong></p>
<p dir='rtl'> برای استفاده در محیط واقعی از  <a href='https://github.com/mthri/zarinpal-django-app/blob/main/zarinpal/views.py'>این </a> درگاه باید <a href='https://github.com/mthri/zarinpal-django-app/blob/main/zarinpal/views.py#L15'>merchand id</a> خود را وارد کنید و آدرس <a href='https://github.com/mthri/zarinpal-django-app/blob/main/zarinpal/views.py#L16'>Callback url</a> خود را به درستی وارد کنید و در نهایت <code>sandbox=True</code> را برابر False قرار دهید یا کلا آن را حذف کنید.</p>

<hr>

<h2 dir='rtl'> بخش ها: </h2>
<p dir='rtl'> 1- پراخت</p>
<p dir='rtl'> 2- مشاهده تراکنش ها</p>
<p dir='rtl'> 3- صفحه نتیجه</p>
<strong>
<p dir='rtl'> با فرض اینکه پروژه را روی سیستم خود و بر روی پورت 8000 اجرا کرده اید</p>
</strong>

<h3 dir='rtl'>پرداخت:</h3>
<p dir='rtl'><a href='http://127.0.0.1:8000/'>http://127.0.0.1:8000</a></p>
<img src='https://raw.githubusercontent.com/mthri/zarinpal-django-app/main/images/p0.png' />

<h3 dir='rtl'>مشاهده تراکنش ها:</h3>
<p dir='rtl'><a href='http://127.0.0.1:8000/transactions'>http://127.0.0.1:8000/transactions</a></p>
<img src='https://raw.githubusercontent.com/mthri/zarinpal-django-app/main/images/p4.png' />


<h3 dir='rtl'>صفحه نتایج:</h3>
<p dir='rtl'>به صورت خودکار ریدایرکت می‌شود</p>
<img src='https://raw.githubusercontent.com/mthri/zarinpal-django-app/main/images/p2.png' />
<img src='https://raw.githubusercontent.com/mthri/zarinpal-django-app/main/images/p3.png' />
<img src='https://raw.githubusercontent.com/mthri/zarinpal-django-app/main/images/p1.png' />

<p dir='rtl'>این اپ بر اساس <a href='https://github.com/Par3ae/Django-Zarinpal'> این پروژه </a> ایجاد شده است.</p>


