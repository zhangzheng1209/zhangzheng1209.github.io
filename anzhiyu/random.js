var posts=["2025/02/09/Kuala Lumpur_2024/","2025/02/08/Kuwait City/","2025/02/09/Muscat_2024/","2025/02/09/Riyadh_2024/","2025/01/22/Rabat_2024/","2025/01/22/mdhelp/","2025/02/09/nizwa_2024/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };