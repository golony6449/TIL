# ListView in Flutter

## 개요

* UI상에 리스트뷰를 구현하는 위젯



## 구현 1

* `Stateful` 위젯, `State` 위젯 2개가 필요
* `ListView.builder`를 이용해 ListView 위젯 생성
* 이때, itemBuilder에, 콜백 함수(==Anonymous Function) 지정
* ​                 ==> 콜백함수는 `context`, `index`를 매개변수로 함
* 콜백함수는 적절한 처리 후, `ListTile` 위젯을 반환하도록 구현

## Example Code

```dart
import 'package:english_words/english_words.dart' as prefix0;
import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();

    return MaterialApp(
      title: 'Flutter Demo',
      home: RandomWords(),
    );
  }
}

class RandomWords extends StatefulWidget{
  @override
  RandomWordsState createState() => RandomWordsState();
}

class RandomWordsState extends State<RandomWords>{
  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18.0);

  @override
  Widget build(BuildContext context) {
    print("build Called");
    final wordPair = WordPair.random();
    return Scaffold(
      appBar: AppBar(
        title: Text("Tutorial"),
      ),
      body: _buildSuggestions(),
    );
  }

  Widget _buildSuggestions(){
    print("buildSuggestions Called");
    return ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemBuilder: (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;
        if (index >= _suggestions.length){
          _suggestions.addAll(prefix0.generateWordPairs().take(10));
        }
        return _buildRow(_suggestions[index]);
      }
    );
  }

  Widget _buildRow(prefix0.WordPair pair){
    print("buildRow Called");
    return ListTile(
      title: Text(
        pair.asPascalCase,
        style: _biggerFont,
      ),
      subtitle: Text("Second Line"),
    );
  }
}
```



## 구현 2

* `ListTile`의 리스트를 생성 (예제에서는 `ListTile.divideTiles` 사용)
* 이를 `ListView`의 `children` 으로 전달

## Example Code

```dart
    // Navigator: 윈도우를 관리하는 Stack. 새 Layout을 여기에 Push함으로서, 화면 전환 가능
    Navigator.of(context).push(
      MaterialPageRoute<void>(
        builder: (BuildContext context){
          final Iterable<ListTile> tiles = _saved.map(
              (WordPair pair) {
                return ListTile(
                  title: Text(
                    pair.asPascalCase,
                    style: _biggerFont,
                  )
                );
              }
          );

          // ListTile에 사이에 가로선 추가
          final List<Widget> divided = ListTile.divideTiles(
            context: context,
            tiles: tiles,
          ).toList();

          return Scaffold(
            appBar: AppBar(
              title: Text('Saved Suggestions')
            ),
            body: ListView(children: divided),  // children: Array of Widget
          );
        }
      )
    );
```

