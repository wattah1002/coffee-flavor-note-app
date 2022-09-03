require 'rails_helper'

RSpec.describe "Users", type: :request do
  describe "GET /new" do
    it "returns http success" do
      # get "/signup"
      get signup_path
      expect(response).to have_http_status(:success)
    end

    it "タイトルに Sign up が含まれること" do
      get signup_path
      expect(response.body).to include "Sign up"
    end
  end

  describe 'POST /users #create' do
    it '無効な値だと登録されないこと' do
      expect {
        post users_path, params: { user: { name: '',
                                           email: 'user@invalid',
                                           password: 'foo',
                                           password_confirmation: 'bar' } }
        }.to_not change(User, :count)
    end

    context '有効な値の場合' do
      let(:user_params) {{ user: { name: 'Example User',
                                   email: 'user@example.com',
                                   password: 'password',
                                   password_confirmation: 'password' } } }

      it '登録されること' do
        expect {
          post users_path, params: user_params
        }.to change(User, :count).by 1
      end

      it 'users/show にリダイレクトされること' do
        post users_path, params: user_params
        user = User.last
        expect(response).to redirect_to user
      end

      it 'flash が表示されること' do
        post users_path, params: user_params
        expect(flash).to be_any
      end
    end
  end
end
