import 'package:flutter/material.dart';
import 'package:flutter_base/commons/app_colors.dart';
import 'package:flutter_base/commons/app_shadow.dart';
import 'package:flutter_base/commons/app_text_styles.dart';
import 'package:flutter_base/models/enums/load_status.dart';
import 'package:flutter_base/ui/pages/farmers_management/add_employee/employee_adding_cubit.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_bar_widget.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_button.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_dropdown_button.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_snackbar.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_text_field.dart';
import 'package:flutter_base/ui/widgets/b_agri/drop_down_picker/app_manager_picker.dart';
import 'package:flutter_base/utils/validators.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class EmployeeAddingPage extends StatefulWidget {
  EmployeeAddingPage({Key? key}) : super(key: key);

  @override
  _EmployeeAddingPageState createState() => _EmployeeAddingPageState();
}

class _EmployeeAddingPageState extends State<EmployeeAddingPage> {
  late EmployeeAddingCubit _cubit;
  final _formKey = GlobalKey<FormState>();
  late TextEditingController nameController;
  late TextEditingController phoneController;
  bool isFirst = false;

  @override
  void initState() {
    _cubit = BlocProvider.of<EmployeeAddingCubit>(context);
    super.initState();

    nameController = TextEditingController();
    phoneController = TextEditingController();

    nameController.addListener(() {
      _cubit.changeName(nameController.text);
    });
    phoneController.addListener(() {
      _cubit.changePhoneNumber(phoneController.text);
    });
  }

  @override
  void dispose() {
    super.dispose();
    nameController.dispose();
    phoneController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBarWidget(
        context: context,
        title: 'Th??m nh??n c??ng',
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 15, vertical: 15),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Form(
                key: _formKey,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'H??? t??n',
                      style: AppTextStyle.greyS18,
                    ),
                    SizedBox(height: 10),
                    AppTextField(
                      hintText: 'Nh???p v??o h??? t??n',
                      controller: nameController,
                      // validator: (value) {
                      //   if (Validator.validateNullOrEmpty(value!))
                      //     return "B???n ch??a nh???p h??? v?? t??n";
                      //   else
                      //     return null;
                      // },
                    ),
                    SizedBox(height: 20),
                    Text(
                      'S??? ??i???n tho???i',
                      style: AppTextStyle.greyS18,
                    ),
                    SizedBox(height: 10),
                    AppTextField(
                      autoValidateMode: isFirst == true
                          ? AutovalidateMode.onUserInteraction
                          : null,
                      hintText: 'Nh???p v??o s??? ??i???n tho???i',
                      controller: phoneController,
                      keyboardType: TextInputType.phone,
                      validator: (value) {
                        if (!Validator.validatePhone(value)) {
                          return "S??? ??i???n tho???i kh??ng ????ng ?????nh d???ng";
                        } else
                          return null;
                      },
                    ),
                    SizedBox(height: 20),
                    Text(
                      'Ch???n qu???n l??',
                      style: AppTextStyle.greyS18,
                    ),
                    SizedBox(height: 10),
                    AppManagerPicker(
                      onChange: (value) {
                        _cubit.changeManagerId(value!.manager_id ?? "");
                      },
                    ),
                  ],
                ),
              ),
              SizedBox(height: 30),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Expanded(
                    child: AppButton(
                      color: AppColors.redButton,
                      title: 'H???y b???',
                      onPressed: () {
                        Navigator.of(context).pop(false);
                      },
                    ),
                  ),
                  SizedBox(width: 25),
                  BlocConsumer<EmployeeAddingCubit, EmployeeAddingState>(
                    bloc: _cubit,
                    listenWhen: (prev, current) {
                      return prev.loadStatus != current.loadStatus;
                    },
                    listener: (context, state) {
                      if (state.loadStatus == LoadStatus.SUCCESS) {
                        _showCreateSuccess();
                      }
                      if (state.loadStatus == LoadStatus.FAILURE) {
                        showSnackBar('C?? l???i x???y ra!');
                      }
                    },
                    builder: (context, state) {
                      return Expanded(
                        child: AppButton(
                          color: AppColors.mainDarker,
                          isEnabled: state.buttonEnabled,
                          isLoading: state.loadStatus == LoadStatus.LOADING
                              ? true
                              : false,
                          title: 'X??c nh???n',
                          onPressed: () async {
                            setState(() {
                              isFirst = true;
                            });
                            if (_formKey.currentState!.validate()) {
                              await _cubit.createFarmer();
                            }
                            // Navigator.of(context).pop(true);
                          },
                        ),
                      );
                    },
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showCreateSuccess() async {
    Navigator.of(context).pop(true);
  }

  void showSnackBar(String message) {
    ScaffoldMessenger.of(context).hideCurrentSnackBar();
    ScaffoldMessenger.of(context).showSnackBar(AppSnackBar(
      message: message,
    ));
  }
}
