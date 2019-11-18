const me = {
  name: '찬우',   // key가 한 단어일 때
  'phone number': '010231412321',    // key가 여러 단어일 때
  appleProducts: {
    iphone: 'xs',
    watch: 'series5',
    macbook: 'pro2019'
  }
}

me.name             // "찬우"
me['name']          // "찬우"
// Key가 여러 단어일 때 []로 접근!
me['phone number']  // "010231412321"

me.appleProducts
//  {iphone: "xs", watch: "series5", macbook: "pro2019"}
me.appleProducts.iphone
//  "xs"