import 'package:bot_toast/bot_toast.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:bruno/bruno.dart';

typedef _addCallBack = void Function(int selectIndex,);
typedef _mzeaddCallBack = void Function(int selectIndex,);
typedef enterDelete = void Function(int selectIndex,);


class CounterPage extends StatefulWidget {

  var count;

  bool isShowDialog;

  final _addCallBack  addcallback;
  final _mzeaddCallBack  mzecallback;
  final _mzeaddCallBack  enterDelete;

  // VoidCallback addvoidCallback;
  // VoidCallback mzevoidCallback;

  CounterPage({this.count =1,required this.addcallback,required this.mzecallback,required this.enterDelete,
    this.isShowDialog=true
  });

  @override
  _CounterPageState createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {



  @override
  Widget build(BuildContext context) {
    return Container(
      child: Row(
        children: [
          Container(

            padding: EdgeInsets.only(bottom: 9),
            child: IconButton(onPressed: (){

              if(widget.count == 1){
                if(widget.isShowDialog==true){
                  BrnDialogManager.showConfirmDialog(context,
                      cancel: '取消', confirm: '确定',message: '确定要删除',title: '温馨提示',onCancel: (){
                        Get.back();
                      },onConfirm: (){
                        widget.enterDelete(widget.count);
                        Navigator.of(context).pop();
                      }
                  );
                }


                // showDialog<Null>(
                //   context: context,
                //   barrierDismissible: false,
                //   builder: (BuildContext context) {
                //     return AlertDialog(
                //       title: const Text('确定要删除'),
                //       content: SingleChildScrollView(
                //         child:  ListBody(
                //           children: const <Widget>[
                //              // Text('确定要删除'),
                //              // Text('内容 2'),
                //           ],
                //         ),
                //       ),
                //       actions: <Widget>[
                //         FlatButton(
                //           child: new Text('取消'),
                //           onPressed: () {
                //             Navigator.of(context).pop();
                //           },
                //         ),
                //          FlatButton(
                //           child: new Text('确定'),
                //           onPressed: () {
                //             widget.enterDelete(widget.count);
                //             Navigator.of(context).pop();
                //           },
                //         ),
                //       ],
                //     );
                //   },
                // ).then((val) {
                //   print(val);
                // });
                // print('确定删除么');
                widget.count == 1;
                return;
              }else{
                widget.count--;
              }
              widget.mzecallback(widget.count,);

              setState(() {

              });
            }, icon: Icon(Icons.minimize_rounded),iconSize: 15,color: Colors.grey,),
          ),
          Container(
            height: 25,
            alignment: Alignment.center,
            width: 35,
            color: Colors.grey.shade200,
            child: Text('${widget.count}',style: TextStyle(fontWeight: FontWeight.w800),),
          ),
          IconButton(onPressed: (){
            widget.count++;
            widget.addcallback(widget.count);
            setState(() {

            });
          }, icon: Icon(Icons.add_rounded),iconSize: 15,color: Colors.grey,),
        ],
      ),
    );
  }
}
