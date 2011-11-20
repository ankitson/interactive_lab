class CreateMySessions < ActiveRecord::Migration
  def self.up
    create_table :my_sessions do |t|
      t.string :session_id
      t.datetime :time
      t.string :ga_utma

      t.timestamps
    end
  end

  def self.down
    drop_table :my_sessions
  end
end
