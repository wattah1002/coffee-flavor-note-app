require 'rails_helper'

RSpec.describe "Users", type: :system do
    before do
        driven_by(:rack_test)
    end

    describe '#create' do
        context '無効な値の場合' do
            it 'エラーメッセージ用の表示領域が描画されていること' do
                visit signup_path
                fill_in 'ユーザー名', with: ''
                fill_in 'メールアドレス', with: 'user@invalid'
                fill_in 'パスワード', with: 'foo'
                fill_in 'パスワード再入力', with: 'bar'
                click_button 'アカウントを作成する'

                expect(page).to have_selector 'div#error_explanation'
            end
        end
    end
end