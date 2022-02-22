# FaceMask Classification


아무래도 오늘 회의에서 너무 제 의견을 밀어붙인거 같기도 하고 말을 유도리있게 전달하지 못한 느낌이있어 혹시나 제대로 전달되지 못한 부분이 있을까 염려가 되어 이렇게 글을 남기게 되었습니다 ㅜ. ㅜ

우선 제가 협업에 관하여 말하고 싶었던 부분은 바로바로 ~~ 

1. 역할 분담을 하지 않았을 경우 대회 마지막 까지 회의 시간때마다 각자 열심히 짠 코드를 공유만 하고 마지막에 가장 성능이 좋게 나온 코드로 제출을 하게 될 수 있습니다

   - 아무래도 역할을 나누지 않게되면 각자만의 코드를 처음부터 끝까지 짜게 될 확률이 굉장히 높다고 생각합니다. 아마 상대의 코드를 이해하는거는 사실 단시간에 이뤄질 수 없다고 생각을 하고(남의 코드를 보면 알겠지만 ,, 내코드와 남이짠코드는 정말 천지차이 ,,), 이렇게 대회내내 진행되게 되면 협업에서의 장점도 살리지 못할 뿐더러 추가적인 내용도 각자 공부하게 될것이고(물론 공유도 하겠지만 각자의 코드가 다르기에 바로 적용될수있냐의 문제도 있고 개인적으로 각자 코드의 성능을 높이는데에 집중하게 될 것 같았습니다-!), 시간적 한계도 있다보니 아무래도 5명이서 낼 수 있는 역량을 충분히 활용하지 못할것이라고 느꼈습니다 

2. 만약에 누군가 어 ! 이부분에서 이렇게 하면 좋을 것같아요 라고 했을 경우 

   - 따로(각자) 베이스라인 코드를 짜서 하나가 선택된 경우(코드 5개중에 잘나온거 1개 선택) : 아마 선택된 코드를 만든 사람만이 그 코드를 완벽하게 이해하고 있을 것이므로 아마 그사람이 계속 코드 수정 또한 진행될 확률이 높음 / 다른사람이 고치고자 할때 처음부터 그 코드를 이해하기 전까지 손대기 쉽지 않을 것이며 상당한 시간이 소요될것에 틀!림없!음
   - 따로 베이스라인 코드를 짜서 각자의 코드에 수정하는 경우(코드 5개 짜서 5개 유지하면서 수정해나가기) : 이 경우에는" 어! 이부분에서 이렇게 하면 좋을 것같아요"는 본인 코드에서 발견한 점일 것이고, 다른사람 코드에 적용이 될지 안될지 미지수임. 그래서 결국 본인 코드 성능을 높이기 위해 본인 코드에 맞춰 여러부분을 찾아볼 것이고 아마 놓치고 넘어가는 부분도 분명 ! 발생할 것임 ! 그렇다고 남이 내코드에서 부족한 부분을 봐주냐 ?? 그것도 아님 ! 왜냐면 본인 코드를 고치고 성능 높이느라 바쁠 것이 틀림없음 .. 진짜진짜진짜루 ...... 

3. 그래서 제가 회의 중에 가장 말하고 싶었던 부분은 무엇이었냐 ~? 

   - 많다면 많을 적다면 적을 코딩 프로젝트를 진행해보면서 항상 느낀점이 각자 책임지고 맡아서하는 부분이 분명 필요하다는 점이었습니다. 물론 우리는 공부하면서 배워나가는데 의의를 두고 있지만, 그래도 프로젝트로 진행되는만큼 이렇게 협업해서 좋은 결과를 내보는것도 충분이 좋은 경험이 될것입니다. 혼자 해나가는 것보다 각 파트에 대해서 더 많은 부분을 깊게 알아 낼수도 있을 거고, 그게 확실하게 공유가 된다는 전제하에 이 프로젝트가 끝나고 난 후에는 분명 정말 많이 성장해 있을 것이라 생각합니다 

   - 역할을 나눈다는 부분에서 살짝 이해가 안갈 수 있다고 생각합니다. 근데 제가 말하고 싶었던것은 그 파트에 대해서 책임? 총괄자 라고 해야할까요? 뭔가 그부분에 있어서는 전체적으로 코드를 확실하게 이해하고 누군가 이거 이렇게 반영해주세요 ~ 예를 들어 **"model 파트인 규리왈 : 제가 efficientNet쓰려면 input size가 고정되있어 우리가 받아오는 이미지에 크기 조정이 필요합니다 !!! dataloader/set 하시는 분 이거 224*224로 크기 조정해주세요~"** 라고 했을 때 바로바로 실행할 수 있는 누군가가 정해져 있는거는 코드 협업에 있어 꼭 필요한 부분이라고 생각했습니다. (정해지지 않는다면 "이거 누가할까요 ..?" 부터 시작해서 누가 이부분을 맡아서 수정할지 정하는데 한세월 ~ 코드 이해하는데 한세월 ~ +  본인의 역할이 사라지는 사람도 생기기 마련!!!입니다**(강조강조)) 앞서 말했듯 가설에서 누가 "이렇게 한번 해보면 어떨까요? " 예를 들어 "어 제가 찾아보니까 ResNet(잘모름)이 앙상블할때 잘먹는대요 !! "라면 이거는 modeling파트니까 5명중에 누가 그부분을 실행에 옮길지 바로바로 나오니깐요 !! 효율성 킹왕짱 협업 필수 

   - 이렇게 했음에도 본인 역할이 적다고 생각하는사람도 있고, 실제로 적게 배당되는 사람도 있을 것입니다. 그런데 그 경우라고 한다면 다른부분에서 더 적용될 수 있는 부분이 있나 찾아볼 수도 있는 것이고 예시코드를 긁어와서 직접 전달해 주는 등 분명 팀의 목표를 달성해 나가는데 있어 본인의 할수있는 일은 끊임없이 대회내내 존재한다고 생각합니다! 팀플도 개개인의 자기주도적 열정에 의해 완성되어 나가는 거니깐요 ✨

   - 다양한 파트를 경험해보고 싶은건 당연하고 저도 모든부분을 다 한번씩 해보고 싶은 마음이 큽니다 . 그래서 저는 대회가 끝나고 다시 처음부터 저만의 f1-score를 높일 수 있도록 공부한 내용을 토대로 코드를 다시 짜볼 생각입니다 !! 

   - 사실 회의중에 제말만 계속 한거같아(심지어 말도 똑바로 전달 못했음.. ) 굉장히 찝찝해서 지하철타고 오는동안 정말 열심히 뇌로 정리하고 집와서 열심히 썼습니다 ........ 제 마음이 부디 전달 되길 바라요 .......

   - 성장은 함께 도모하는것🍀 --> 요새 제가 밀고나가는 말입니다 ㅎㅎ 남은 10일동안 함께 달려나가 보자구요 ~ 💪

   - 다 읽고 나면 내용은 싹 비울게요 !! 

     
