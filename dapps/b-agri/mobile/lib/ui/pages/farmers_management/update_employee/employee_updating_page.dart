import 'package:flutter/material.dart';
import 'package:flutter_base/commons/app_colors.dart';
import 'package:flutter_base/commons/app_text_styles.dart';
import 'package:flutter_base/models/enums/load_status.dart';
import 'package:flutter_base/ui/pages/farmers_management/update_employee/employee_updating_cubit.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_bar_widget.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_button.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_snackbar.dart';
import 'package:flutter_base/ui/widgets/b_agri/app_text_field.dart';
import 'package:flutter_base/ui/widgets/b_agri/drop_down_picker/app_manager_picker.dart';
import 'package:flutter_base/utils/validators.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class EmployeeUpdatingPage extends StatefulWidget {
  String farmerId;

  EmployeeUpdatingPage({Key? key, required this.farmerId}) : super(key: key);

  @override
  _EmployeeUpdatingPageState createState() => _EmployeeUpdatingPageState();
}

class _EmployeeUpdatingPageState extends State<EmployeeUpdatingPage> {
  late EmployeeUpdatingCubit _cubit;
  final _formKey = GlobalKey<FormState>();
  late TextEditingController nameController;
  late TextEditingController phoneController;

  @override
  void initState() {
    _cubit = BlocProvider.of<EmployeeUpdatingCubit>(context);
    super.initState();
    _cubit.getFarmerDetail(widget.farmerId);

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
    // TODO: implement dispose
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
        title: 'S???a nh??n c??ng',
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 15, vertical: 15),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              BlocConsumer<EmployeeUpdatingCubit, EmployeeUpdatingState>(
                listenWhen: (prev, current) =>
                    prev.farmerDetail != current.farmerDetail,
                listener: (context, state) {
                  nameController.text = state.fullName ?? "";
                  phoneController.text = state.phoneNumber ?? "";
                },
                builder: (context, state) {
                  return Form(
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
                          enable: state.loadStatus == LoadStatus.LOADING
                              ? false
                              : true,
                          hintText: 'Nh???p v??o h??? t??n',
                          controller: nameController,
                          validator: (value) {
                            if (Validator.validateNullOrEmpty(value!))
                              return "ch??a nh???p";
                            else
                              return null;
                          },
                        ),
                        SizedBox(height: 20),
                        Text(
                          'S??? ??i???n tho???i',
                          style: AppTextStyle.greyS18,
                        ),
                        SizedBox(height: 10),
                        AppTextField(
                          autoValidateMode: AutovalidateMode.onUserInteraction,
                          enable: state.loadStatus == LoadStatus.LOADING
                              ? false
                              : true,
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
                          managerId: state.loadStatus == LoadStatus.SUCCESS
                              ? state.managerId
                              : null,
                          onChange: state.loadStatus == LoadStatus.LOADING
                              ? null
                              : (value) {
                                  _cubit
                                      .changeManagerId(value!.manager_id ?? "");
                                },
                        ),
                        SizedBox(height: 30),
                      ],
                    ),
                  );
                },
              ),
              Column(
                children: [
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
                      BlocConsumer<EmployeeUpdatingCubit,
                          EmployeeUpdatingState>(
                        bloc: _cubit,
                        listenWhen: (prev, current) {
                          return prev.loadStatus != current.loadStatus;
                        },
                        listener: (context, state) {
                          if (state.loadStatus == LoadStatus.SUCCESS) {
                            _showUpdateSuccess();
                          }
                          if (state.loadStatus == LoadStatus.FAILURE) {
                            showSnackBar('C?? l???i x???y ra!');
                          }
                        },
                        builder: (context, state) {
                          return Expanded(
                            child: AppButton(
                              color: AppColors.main,
                              title: 'X??c nh???n',
                              isEnabled: state.buttonEnabled,
                              isLoading: state.loadStatus == LoadStatus.LOADING
                                  ? true
                                  : false,
                              onPressed: () async {
                                // _formKey.currentState!.validate();
                                await _cubit.updateFarmer(widget.farmerId);
                                Navigator.of(context).pop(true);
                              },
                            ),
                          );
                        },
                      ),
                    ],
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showUpdateSuccess() async {
    Navigator.of(context).pop(true);
  }

  void showSnackBar(String message) {
    ScaffoldMessenger.of(context).hideCurrentSnackBar();
    ScaffoldMessenger.of(context).showSnackBar(AppSnackBar(
      message: message,
    ));
  }
}
