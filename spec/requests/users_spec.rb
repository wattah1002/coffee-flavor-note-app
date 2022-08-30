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
  end
end
